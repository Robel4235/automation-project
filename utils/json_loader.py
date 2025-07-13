import json
import os

def load_json(path):
    with open(path, 'r') as file:
        return json.load(file)

def get_all_json_files(directory):
    return [
        os.path.join(directory,filename)
        for filename in os.listdir(directory)
        if filename.endswith(".json")
    ]
