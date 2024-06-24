import csv
import json
from bs4 import BeautifulSoup
import sys

maxInt = sys.maxsize

while True:

    try:
        csv.field_size_limit(maxInt)
        break
    except OverflowError:
        maxInt = int(maxInt/10)

# Function to clean HTML content and extract text
def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text().strip()

# Function to remove all newline characters from text
def remove_newlines(text):
    # Remove all occurrences of \\n
    text = text.replace('\\n', ' ')
    text = text.replace('\\','')
    # Replace single \n, \r, \r\n and multiple \n\n\n with a single space
    return ' '.join(text.replace('\r\n', ' ').replace('\n', ' ').replace('\r', ' ').split())

# Function to convert CSV data to JSON with a specified number of rows
def csv_to_json(csv_file, num_rows=None):
    # Initialize a list to hold JSON objects
    json_data = []

    # Open and read the CSV file
    with open(csv_file, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Iterate through rows up to num_rows if specified
        for idx, row in enumerate(reader):
            if num_rows is not None and idx >= num_rows:
                break  # Stop processing rows if num_rows is specified and reached
            
            # Clean problem HTML content
            problem_text = clean_html(row['problem_html'])
            problem_text = remove_newlines(problem_text)
            
            # Clean solutions HTML content
            solutions = []
            for i in range(1, 6):  # Assuming solutions_1 to solutions_5 are present
                solution_html = row.get(f'solution_{i}', '')
                if solution_html:
                    solution_text = clean_html(solution_html)
                    solution_text = remove_newlines(solution_text)
                    solutions.append(solution_text)
            
            # Create a JSON object for the current row
            json_object = {
                'category': row['category'],
                'contest': row['contest'],
                'link': row['link'],
                'name': row['name'],
                'source': row['source'],
                'problem': problem_text,
                'solutions': solutions
            }
            
            # Append the JSON object to the list
            json_data.append(json_object)
    
    return json_data

json_data = csv_to_json('aops.csv', num_rows=35000)

# Write JSON data to a file
output_file = 'output.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=4)

print(f'JSON data has been written to {output_file}')
