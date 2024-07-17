import os
import requests
import json


new_folder = 'json_files'
os.makedirs(new_folder, exist_ok=True)

response = requests.get('https://jsonplaceholder.typicode.com/posts')
data = response.json()

for index, item in enumerate(data):
    filename = f'{new_folder}/json_{index + 1}.json'
    with open(filename, 'w') as file:
        json.dump(item, file, indent=4)


