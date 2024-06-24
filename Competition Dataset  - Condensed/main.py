import os
import json

train_folder_path = 'test'

# Traverse through each subfolder in the "train" directory
for subfolder in os.listdir(train_folder_path):
    subfolder_path = os.path.join(train_folder_path, subfolder)
    
    # Check if the path is a directory
    if os.path.isdir(subfolder_path):
        combined_data = []

        # Traverse through each JSON file in the subfolder
        for json_file in os.listdir(subfolder_path):
            json_file_path = os.path.join(subfolder_path, json_file)

            # Read the JSON file and append its content to the combined_data list
            if json_file.endswith('.json'):
                with open(json_file_path, 'r') as file:
                    data = json.load(file)
                    combined_data.append(data)

        # Write the combined data to a single JSON file in the subfolder
        output_file_path = os.path.join(subfolder_path, 'combined.json')
        with open(output_file_path, 'w') as output_file:
            json.dump(combined_data, output_file, indent=4)
