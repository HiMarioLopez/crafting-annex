import json
import os
from collections import defaultdict

def split_json_by_nested_id(input_file, output_base_dir):
    # Load the JSON data with UTF-8 encoding
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # Dictionary to hold grouped entries
    grouped_data = defaultdict(list)
    
    # Process each entry in the JSON data
    for entry in data:
        # Extract the Id field
        item_id = entry.get('Id')
        if item_id and item_id.startswith('Metadata/Items'):
            # Remove the 'Metadata/Items' prefix
            relevant_path = item_id[len('Metadata/Items/'):]
            # Split the remaining path by '/'
            path_parts = relevant_path.split('/')
            # Use all but the last part of the Id for directories
            if len(path_parts) > 1:
                group_key = '/'.join(path_parts[:-1])
                grouped_data[group_key].append(entry)
    
    # Write each group to a corresponding file
    for group_key, entries in grouped_data.items():
        # Create the directory path based on the reduced Id
        directory_path = os.path.join(output_base_dir, group_key)
        # Ensure the directory exists
        os.makedirs(directory_path, exist_ok=True)
        # Define the output file name based on the last part of the Id
        file_name = f"{group_key.split('/')[-1]}.json"
        output_file_path = os.path.join(directory_path, file_name)
        # Write the grouped entries to the file
        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            json.dump(entries, outfile, indent=4)
    
    print("Data successfully grouped and saved into a nested directory structure based on the Id path after 'Metadata/Items/'.")

# Example usage:
input_file = 'baseitemtypes.json'  # Replace with your actual file path
output_base_dir = 'split_files/baseitemtypes'  # Base directory to save the grouped files

split_json_by_nested_id(input_file, output_base_dir)
