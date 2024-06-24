import json

with open('math.jsonl', 'r') as file:
    json_lines = file.readlines()

extracted_data = []
for line in json_lines:
    json_obj = json.loads(line)
    extracted_obj = {
        "question": json_obj["question"],
        "solution": json_obj["other"]["solution"],
        "level": json_obj["other"]["level"],
        "type": json_obj["other"]["type"]
    }
    extracted_data.append(extracted_obj)

formatted_json = json.dumps(extracted_data, indent=4)

with open('other_math.json', 'w') as file:
    file.write(formatted_json)

print("Selected fields have been extracted and saved to a formatted JSON file.")