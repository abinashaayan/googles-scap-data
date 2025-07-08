import os
import csv
import json

DATA_DIR = os.path.join(os.path.dirname(__file__), 'Data')
CSV_DIR = os.path.join(DATA_DIR, 'csv')
JSON_DIR = os.path.join(DATA_DIR, 'json')

def list_cities_and_categories(data_type):
    base_dir = CSV_DIR if data_type == 'csv' else JSON_DIR
    cities = [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]
    city_cat_map = {}
    for city in cities:
        city_path = os.path.join(base_dir, city)
        files = [f for f in os.listdir(city_path) if f.endswith('.' + data_type)]
        categories = [os.path.splitext(f)[0] for f in files]
        city_cat_map[city] = categories
    return city_cat_map

def select_option(options, prompt):
    print(f"\n{prompt}")
    for idx, opt in enumerate(options, 1):
        print(f"{idx}. {opt}")
    while True:
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(options):
                return options[choice - 1]
        except ValueError:
            pass
        print("Invalid choice. Try again.")

def view_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            print(', '.join(row))

def view_json(file_path):
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        print(json.dumps(data, indent=2, ensure_ascii=False))

def main():
    data_type = select_option(['csv', 'json'], 'Select data type to view:')
    city_cat_map = list_cities_and_categories(data_type)
    if not city_cat_map:
        print(f"No {data_type.upper()} data found.")
        return
    cities = list(city_cat_map.keys())
    city = select_option(cities, 'Select a city:')
    categories = city_cat_map[city]
    if not categories:
        print(f"No categories found for {city}.")
        return
    category = select_option(categories, 'Select a category:')
    file_path = os.path.join(CSV_DIR if data_type == 'csv' else JSON_DIR, city, f"{category}.{data_type}")
    print(f"\n--- Contents of {file_path} ---\n")
    if data_type == 'csv':
        view_csv(file_path)
    else:
        view_json(file_path)

if __name__ == '__main__':
    main() 