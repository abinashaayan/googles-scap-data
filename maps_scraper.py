import sys
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException


def scrape_google_maps(url, max_results=50):
    # Set up Selenium with headless Chrome
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)
    time.sleep(5)  # Wait for page to load

    results = []
    scrollable_div = None

    # Try to find the scrollable results pane
    try:
        scrollable_div = driver.find_element(By.XPATH, '//div[contains(@aria-label, "Results for")]')
    except NoSuchElementException:
        try:
            scrollable_div = driver.find_element(By.XPATH, '//div[@role="feed"]')
        except NoSuchElementException:
            print("Could not find results pane. Exiting.")
            driver.quit()
            return []

    last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
    scroll_attempts = 0
    while len(results) < max_results and scroll_attempts < 20:
        # Extract all result cards
        cards = driver.find_elements(By.XPATH, '//div[contains(@aria-label, "Results for")]/div[contains(@data-result-index, "")]')
        if not cards:
            cards = driver.find_elements(By.XPATH, '//div[@role="article"]')
        for card in cards:
            try:
                name = card.find_element(By.XPATH, './/div[contains(@aria-label, "Result")]//div[contains(@class, "fontHeadlineSmall") or contains(@class, "qBF1Pd") or contains(@class, "fontBodyMedium")]').text
            except NoSuchElementException:
                name = ""
            try:
                address = card.find_element(By.XPATH, './/div[contains(@class, "W4Efsd") or contains(@class, "fontBodyMedium")]').text
            except NoSuchElementException:
                address = ""
            try:
                rating = card.find_element(By.XPATH, './/span[contains(@aria-label, "stars")]').text
            except NoSuchElementException:
                rating = ""
            entry = {"Name": name, "Address": address, "Rating": rating}
            if entry not in results:
                results.append(entry)
        # Scroll down
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scrollable_div)
        time.sleep(2)
        new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_div)
        if new_height == last_height:
            scroll_attempts += 1
        else:
            scroll_attempts = 0
        last_height = new_height
    driver.quit()
    return results[:max_results]


def main():
    if len(sys.argv) < 2:
        print("Usage: python maps_scraper.py <google_maps_search_url>")
        sys.exit(1)
    url = sys.argv[1]
    if not url.startswith("https://www.google.com/maps/search/"):
        print("Please provide a valid Google Maps search URL.")
        sys.exit(1)
    print("Scraping Google Maps search results...")
    data = scrape_google_maps(url)
    if not data:
        print("No data found or failed to scrape.")
        sys.exit(1)
    
    # Configure pandas display options
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', None)
    
    df = pd.DataFrame(data)
    
    # Print the dataframe with full width
    with pd.option_context('display.max_rows', None, 
                          'display.max_columns', None, 
                          'display.width', None, 
                          'display.max_colwidth', None):
        print(df)

if __name__ == "__main__":
    main()