from scipy.spatial import KDTree
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color

import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
COLORS_FILE_PATH = os.path.join(current_dir, '..', 'data', 'colors.json')

# Precompute Lab values
with open(COLORS_FILE_PATH, 'r') as file:
    color_data = json.load(file)
    PRECOMPUTED_LAB_COLORS = {name: convert_color(sRGBColor.new_from_rgb_hex(value), LabColor) for value, name in color_data.items()}

# Convert the Lab colors to a list of tuples for KDTree
lab_values = [color.get_value_tuple() for color in PRECOMPUTED_LAB_COLORS.values()]
color_names = list(PRECOMPUTED_LAB_COLORS.keys())

# Build a KDTree with Lab values
lab_kdtree = KDTree(lab_values)

def get_closest_color(rgb : list) -> str:
    input_rgb = sRGBColor(rgb[0], rgb[1], rgb[2], is_upscaled=True)
    input_lab = convert_color(input_rgb, LabColor)
    input_lab_tuple = input_lab.get_value_tuple()

    # Query the KDTree for the closest color
    distance, index = lab_kdtree.query(input_lab_tuple)
    return color_names[index]

def to_hex(r: int, g: int, b: int) -> str:
    return "#{:02x}{:02x}{:02x}".format(r, g, b)