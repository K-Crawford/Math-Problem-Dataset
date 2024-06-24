import json

# Read the JSONL file
with open('sat-math.jsonl', 'r') as file:
    json_lines = file.readlines()

# Extract the required fields from each JSON object
extracted_data = []
for line in json_lines:
    json_obj = json.loads(line)
    extracted_obj = {
        "question": json_obj["question"],
        "options": json_obj["options"],
        "correct_answer": json_obj["label"],
        "solution": json_obj["other"]["solution"]
    }
    extracted_data.append(extracted_obj)

# Convert the list of extracted JSON objects to a nicely formatted JSON string
formatted_json = json.dumps(extracted_data, indent=4)

# Save the formatted JSON to a new file
with open('sat_math.json', 'w') as file:
    file.write(formatted_json)

print("Selected fields have been extracted and saved to a formatted JSON file.")
