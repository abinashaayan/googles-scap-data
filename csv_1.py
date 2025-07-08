import json
import csv
import os

def json_to_csv(json_file, csv_file):
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    if isinstance(data, list):
        # Assuming all JSON objects have the same structure,
        # we'll use the keys of the first object as the header for CSV
        header = list(data[0].keys())
        
        with open(csv_file, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=header)
            writer.writeheader()
            writer.writerows(data)
    else:
        print(f"Invalid JSON format in file: {json_file}")

def convert_multiple_json_to_csv(json_dir, csv_dir):
    # Create CSV directory if it doesn't exist
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)

    # Iterate over each JSON file in the directory
    for json_file in os.listdir(json_dir):
        if json_file.endswith('.json'):
            # Construct paths for JSON and CSV files
            json_path = os.path.join(json_dir, json_file)
            csv_file = os.path.splitext(json_file)[0] + '.csv'
            csv_path = os.path.join(csv_dir, csv_file)
            
            # Convert JSON to CSV
            json_to_csv(json_path, csv_path)



# Example usage:
json_directory = './Data/Ahmedabad'
csv_directory = './Data/csv/Ahmedabad'
convert_multiple_json_to_csv(json_directory, csv_directory)
