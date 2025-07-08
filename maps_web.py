import streamlit as st
import pandas as pd
import sys
import time
import io
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

# --- Scraper function (extract all visible fields, including website and labels) ---
def scrape_google_maps(url, max_results=50):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(url)
    time.sleep(5)
    results = []
    scrollable_div = None
    try:
        scrollable_div = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Results for")]')
    except NoSuchElementException:
        try:
            scrollable_div = driver.find_element(By.XPATH, '//div[@role="feed"]')
        except NoSuchElementException:
            driver.quit()
            return []
    # Scroll to load more results
    last_count = 0
    scroll_attempts = 0
    while True:
        cards = driver.find_elements(By.XPATH, '//div[contains(@aria-label, "Results for")]/div[contains(@data-result-index, "")]')
        if not cards:
            cards = driver.find_elements(By.XPATH, '//div[@role="article"]')
        if len(cards) >= max_results or scroll_attempts > 10:
            break
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
        time.sleep(2)
        if len(cards) == last_count:
            scroll_attempts += 1
        else:
            scroll_attempts = 0
        last_count = len(cards)
    # Now process up to max_results cards
    for i, card in enumerate(cards[:max_results]):
        try:
            driver.execute_script("arguments[0].scrollIntoView();", card)
            time.sleep(1)
            card.click()
            time.sleep(3)
        except ElementClickInterceptedException:
            continue
        except Exception:
            continue
        # Now scrape details from the side panel
        try:
            name = driver.find_element(By.XPATH, '//h1[contains(@class, "fontHeadlineLarge") or contains(@class, "DUwDvf")]').text
        except NoSuchElementException:
            name = ""
        try:
            address = driver.find_element(By.XPATH, '//button[contains(@data-item-id, "address") or contains(@aria-label, "Address") or contains(@data-tooltip, "Copy address")]/div[normalize-space()]').text
        except NoSuchElementException:
            try:
                address = driver.find_element(By.XPATH, '//div[contains(@data-item-id, "address") or contains(@aria-label, "Address")]').text
            except NoSuchElementException:
                address = ""
        try:
            timing = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Hours") or contains(@class, "OqCZI") or contains(@class, "cX2WmPgCkHi__open-now-text")]').text
        except NoSuchElementException:
            timing = ""
        try:
            website = driver.find_element(By.XPATH, '//a[contains(@data-item-id, "authority") or contains(@aria-label, "Website")]').get_attribute('href')
        except NoSuchElementException:
            website = ""
        try:
            phone = driver.find_element(By.XPATH, '//button[contains(@data-item-id, "phone:") or contains(@aria-label, "Phone")]/div[normalize-space()]').text
        except NoSuchElementException:
            try:
                phone = driver.find_element(By.XPATH, '//div[contains(@data-item-id, "phone:") or contains(@aria-label, "Phone")]').text
            except NoSuchElementException:
                phone = ""
        try:
            plus_code = driver.find_element(By.XPATH, '//button[contains(@data-item-id, "oloc:") or contains(@aria-label, "Plus code")]/div[normalize-space()]').text
        except NoSuchElementException:
            try:
                plus_code = driver.find_element(By.XPATH, '//div[contains(@data-item-id, "oloc:") or contains(@aria-label, "Plus code")]').text
            except NoSuchElementException:
                plus_code = ""
        try:
            rating = driver.find_element(By.XPATH, '//span[contains(@aria-label, "stars")]').text
        except NoSuchElementException:
            rating = ""
        # Collect all visible labels (e.g., LGBTQ+ friendly, women-owned)
        labels = []
        try:
            label_els = driver.find_elements(By.XPATH, '//div[contains(@aria-label, "Attributes") or contains(@class, "RcCsl")]/div[contains(@class, "fontBodyMedium")]')
            for el in label_els:
                txt = el.text.strip()
                if txt:
                    labels.append(txt)
        except Exception:
            pass
        labels_str = ", ".join(labels)
        try:
            map_direction = driver.find_element(By.XPATH, '//a[contains(@aria-label, "Directions")]').get_attribute('href')
        except NoSuchElementException:
            map_direction = ""
        results.append({
            "Name": name,
            "Address": address,
            "Timing": timing,
            "Website": website,
            "Phone": phone,
            "Plus Code": plus_code,
            "Rating": rating,
            "Labels": labels_str,
            "Map Direction": map_direction
        })
        # Go back to results list
        try:
            back_btn = driver.find_element(By.XPATH, '//button[@aria-label="Back"]')
            back_btn.click()
            time.sleep(2)
        except Exception:
            pass
    driver.quit()
    return results

# --- Custom CSS for a modern, attractive look ---
st.markdown(
    """
    <style>
    body {
        background: #f5f7fa;
    }
    .main .block-container {
        max-width: 1000px !important;
        margin: 0 auto !important;
        padding-left: 0 !important;
        padding-right: 0 !important;
    }
    .st-emotion-cache-1w723zb {
        max-width: 1000px !important;
        margin: 0 auto !important;
        width: 100%;
        padding-left: 0 !important;
        padding-right: 0 !important;
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    .header-card {
        background: linear-gradient(90deg, #4285F4 0%, #34A853 100%);
        color: white;
        border-radius: 1.5rem;
        padding: 2rem 2.5rem 1.5rem 2.5rem;
        margin-bottom: 2rem;
        box-shadow: 0 4px 24px 0 rgba(66,133,244,0.15);
        text-align: center;
    }
    .input-card {
        background: #fff;
        border-radius: 1.25rem;
        padding: 2rem 2rem 1.5rem 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 2px 16px 0 rgba(60,64,67,0.07);
    }
    .stTextInput>div>div>input {
        border-radius: 0.75rem;
        border: 1.5px solid #4285F4;
        font-size: 1.1rem;
        padding: 0.5rem 1rem;
    }
    .stButton>button {
        background: linear-gradient(90deg, #4285F4 0%, #34A853 100%);
        color: white;
        border-radius: 0.75rem;
        font-size: 1.1rem;
        padding: 0.5rem 2rem;
        border: none;
        transition: background 0.3s;
        box-shadow: 0 2px 8px 0 rgba(66,133,244,0.10);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #34A853 0%, #4285F4 100%);
        color: #fff;
    }
    .stDataFrame {
        border-radius: 1rem;
        overflow: hidden;
        box-shadow: 0 2px 16px 0 rgba(60,64,67,0.07);
        margin-top: 1.5rem;
        width: 100% !important;
    }
    .stDataFrame table {
        width: 100% !important;
    }
    .stDataFrame thead, .stDataFrame tbody, .stDataFrame tr, .stDataFrame th, .stDataFrame td {
        width: 100% !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header ---
st.markdown(
    """
    <div class="header-card">
        <h1 style="margin-bottom:0.2em; font-size:2.6rem; font-weight:800; letter-spacing:-1px;">🗺️ Google Maps Search Scraper</h1>
        <p style="font-size:1.2rem; margin-top:0.5em;">Paste a <b>Google Maps search URL</b> below and extract business data in seconds.<br>Fast, easy, and beautiful! 🚀</p>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Main Content Container ---
with st.container():
    # --- Input Card ---
    st.markdown('<div class="input-card">', unsafe_allow_html=True)
    url = st.text_input("Google Maps Search URL", "", help="Paste a URL like https://www.google.com/maps/search/it+company+in+lucknow/")
    st.markdown('</div>', unsafe_allow_html=True)

    # --- Scrape Button and Results ---
    if st.button("Scrape 🚦"):
        if not url.startswith("https://www.google.com/maps/search/"):
            st.error("❌ Please provide a valid Google Maps search URL.")
        else:
            with st.spinner("Scraping Google Maps search results..."):
                data = scrape_google_maps(url)
            if not data:
                st.warning("⚠️ No data found or failed to scrape. Make sure the URL is correct and try again.")
            else:
                df = pd.DataFrame(data)
                st.success(f"✅ Found {len(df)} results!")
                st.dataframe(df, use_container_width=True)
                # Download buttons
                csv = df.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name='google_maps_data.csv',
                    mime='text/csv',
                )
                excel_buffer = io.BytesIO()
                with pd.ExcelWriter(excel_buffer, engine='openpyxl') as writer:
                    df.to_excel(writer, index=False)
                excel_buffer.seek(0)
                st.download_button(
                    label="Download Excel",
                    data=excel_buffer,
                    file_name='google_maps_data.xlsx',
                    mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
                ) 