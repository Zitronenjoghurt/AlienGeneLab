from .color import get_closest_color, to_hex
from ..classes.config import Config

def handle_part_type(part, type_name, value) -> str:
    match type_name:
        case 'color':
            return handle_color(value)
        case 'personality':
            return handle_personality(part, value)
        
    value_name = extract_first_key(value)
    match value_name:
        case 'value':
            return extract_first_value(value)
    
    return None

def handle_color(colors):
    red = colors.get("red", 0)
    green = colors.get("green", 0)
    blue = colors.get("blue", 0)

    return get_closest_color(to_hex(red, green, blue))

def handle_personality(part, personalities):
    config = Config.get_instance()
    expression = config.get_personality_expression()
    personality_depth = part.get('personality_depth', 0)["value"]

    # Get the amount of expressed personalities
    personality_count = 0
    for requirement, count in expression.items():
        if personality_depth >= requirement:
            personality_count = count
    
    if personality_count == 0:
        return ""
    
    # Sort personalities
    personalities = {personality: value for personality, value in sorted(personalities.items(), key=lambda item: item[1], reverse=True)}

    return ', '.join(list(personalities.keys())[:personality_count])

def extract_first_key(dict):
    return list(dict.keys())[0]

def extract_first_value(dict):
    return list(dict.values())[0]