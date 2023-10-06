import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
REPLACE_VALUES_FILE_PATH = os.path.join(current_dir, '..', 'data', 'replace_values.json')

REPLACE_VALUES = None
with open(REPLACE_VALUES_FILE_PATH, 'r') as file:
        REPLACE_VALUES = json.load(file)

def find_key(key) -> list|None:
    for entry in REPLACE_VALUES.values():
          if key in entry['keys']:
                return entry['replacement']
    return None

def replace_from_key(key, value, min_val, max_val) -> str|None:
    labels = find_key(key)
    if not labels:
        return None
    
    return replace(value, min_val, max_val, labels)

def replace(value, min_val, max_val, labels) -> str|None:
    if value < min_val or value > max_val:
        return None
    
    segment_length = (max_val - min_val) / (len(labels) - 1)
    index = int((value - min_val) / segment_length)
    index = min(index, len(labels) - 1)

    return labels[index]