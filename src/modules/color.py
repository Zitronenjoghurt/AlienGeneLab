import numpy as np

# patch deprecated numpy asscalar
def patch_asscalar(a):
    return a.item()
setattr(np, "asscalar", patch_asscalar)

from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
COLORS_FILE_PATH = os.path.join(current_dir, '..', 'data', 'colors.json')

def to_hex(r, g, b):
    return "#{:02x}{:02x}{:02x}".format(r, g, b)

def get_closest_color(hex):
    colors = None
    with open(COLORS_FILE_PATH, 'r') as file:
        colors = json.load(file)
    
    differences = []
    for value, name in colors.items():
        differences.append((name, color_difference(hex, value)))
    
    return min(differences, key = lambda x: x[1])[0]

def color_difference(hex1, hex2):
    # Convert HEX to RGB
    rgb1 = sRGBColor.new_from_rgb_hex(hex1)
    rgb2 = sRGBColor.new_from_rgb_hex(hex2)
    
    # Convert RGB to Lab Color Space (needed for Delta E calculation)
    lab1 = convert_color(rgb1, LabColor)
    lab2 = convert_color(rgb2, LabColor)
    
    # Calculate Delta E
    delta_e = delta_e_cie2000(lab1, lab2)
    
    # The smaller, the smaller the color difference
    return delta_e