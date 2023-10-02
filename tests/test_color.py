from src.modules.color import to_hex, color_difference, get_closest_color

def test_to_hex():
    assert to_hex(255, 255, 255) == "#ffffff"
    assert to_hex(255, 0, 255) == "#ff00ff"
    assert to_hex(1, 255, 0) == "#01ff00"

def test_color_difference():
    assert color_difference("#000000", "#000000") == 0

def test_get_closest_color():
    assert get_closest_color("#FF0000") == "red"
    assert get_closest_color("#999999") == "darkgray"