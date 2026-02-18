"""
JSON Parsing Demo in Python
This script demonstrates how to parse JSON data and convert Python objects to JSON.
"""

import json

# Sample JSON string (as received from an API)
json_string = '''
{
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "year": 1925,
    "genres": ["Fiction", "Classic"],
    "available": true
}
'''

# Parse JSON string to Python dictionary
book = json.loads(json_string)

# Access data from the parsed JSON
print("Title:", book["title"])
print("Author:", book["author"])
print("Year:", book["year"])
print("Genres:", ", ".join(book["genres"]))
print("Available:", book["available"])

# Modify the data
book["rating"] = 4.5
book["genres"].append("Literary")

# Convert Python dictionary back to JSON string
json_output = json.dumps(book, indent=4)
print("\nModified JSON:")
print(json_output)