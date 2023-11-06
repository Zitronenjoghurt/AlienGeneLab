import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
REPLACE_VALUES_FILE_PATH = os.path.join(current_dir, '..', 'data', 'replace_values.json')

REPLACE_VALUES = None
with open(REPLACE_VALUES_FILE_PATH, 'r') as file:
        REPLACE_VALUES = json.load(file)

def find_key(key: str) -> dict|None:
    for entry in REPLACE_VALUES.values():
          if key in entry['keys']:
                return entry
    return find_by_identifier(key)

def find_by_identifier(key: str) -> dict|None:
    entry = REPLACE_VALUES.get(key, None)

    if not entry:
        return None
    
    return entry

def replace_from_key(key: str, value: int, min_val: int, max_val: int, show_percentage: bool = False) -> str:
    entry = find_key(key)
    if not entry:
        return str(value)
    
    return replace(value, min_val, max_val, entry, show_percentage)

def replace(value: int, min_val: int, max_val: int, entry: dict, show_percentage: bool = False) -> str:
    if value < min_val or value > max_val:
        return str(value)
    
    result = ""
    if value == min_val:
         result = entry.get("min_label")
    elif value == max_val:
         result = entry.get("max_label")
    else:
        labels = entry.get("labels")
        segment_length = (max_val - min_val) / (len(labels) - 1)
        index = round((value - min_val) / segment_length)
        index = min(index, len(labels) - 1)
        result = labels[index]
    
    if show_percentage:
        percentage = round((value / max_val) * 100, 1)
        result += f' ({percentage}%)'

    return result