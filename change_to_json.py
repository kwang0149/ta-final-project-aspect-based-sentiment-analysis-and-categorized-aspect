import json

def parse_line(line):
    # Split the line into text and annotations
    parts = line.split("#### #### ####")
    
    # Extract text
    text = parts[0].strip()
    
    # Extract and parse each set of annotations
    annotations = eval(parts[1])
    
    # Process each set of annotations
    labels = []
    for annotation in annotations:
        start_indices, end_indices, polarity = annotation
        # Extract opinion from the text
        opinion = text[start_indices[0]:end_indices[-1]+1].strip()
        # Extract aspect from the text (assuming the aspect is one word)
        aspect = text[start_indices[0] - 2:start_indices[0]].strip()  # Adjust as needed
        labels.append({
            "aspect": aspect,
            "opinion": opinion,
            "polarity": polarity,
            "category": "NULL"
        })
    
    return {
        "text": text,
        "labels": labels
    }

# Read input text file with explicit encoding (UTF-8)
with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Parse each line and create a list of dictionaries
data_list = [parse_line(line) for line in lines]

# Write the list of dictionaries to a JSON file
with open('output.json', 'w') as json_file:
    json.dump(data_list, json_file, indent=2)