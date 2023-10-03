from .color import get_closest_color, to_hex

def handle_part_type(part, type, value) -> str:
        if type == "color":
            return handle_color(value)
        
        return None

def handle_color(colors):
      red = colors.get("red", 0)
      green = colors.get("green", 0)
      blue = colors.get("blue", 0)

      return get_closest_color(to_hex(red, green, blue))