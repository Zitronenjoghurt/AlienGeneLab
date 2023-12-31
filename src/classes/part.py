from ..modules.color import get_closest_color, to_hex
from ..modules.value_replacer import replace_from_key
from .config import Config
from .gene_library import GeneLibrary

# A body part included in the phenotype of an alien
class Part:
    def __init__(self, name: str, developing_value_type: str, developing_value) -> None:
        self.name = name
        if len(developing_value_type) != 0:
            self.develop = {}
            self.develop[developing_value_type] = developing_value
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, self.__class__):
            return self.__dict__ == __value.__dict__
        return False

    def add_value(self, type: str, effect: str, value) -> None:
        if len(effect) == 0:
            setattr(self, type, value)
            return
        
        property = getattr(self, type, None)
        if not property:
            setattr(self, type, {effect: value})
            return
        
        property[effect] = value
    
    def get_name(self) -> str:
        return self.name

    def get_properties(self) -> list:
        return list(self.__dict__.keys())
    
    def get_property_value(self, property: str, default = None) -> object:
        return getattr(self, property, default)

    def to_description(self) -> dict:
        properties = self.get_properties()
        
        description = {}
        for property in properties:
            key, value = self.__handle_property(property)
            if key is not None:
                description[key] = value
        
        return description

    def __handle_property(self, property: str) -> tuple:
        value = self.get_property_value(property)
        
        match property:
            case "name":
                return None, None
            case "color":
                return "color", self.__handle_color(value)
            case "personality":
                return "personality", self.__handle_personality(value)
            case "develop":
                return self.__handle_develop(value)
            case "texture":
                return "texture", self.__handle_texture(value)
            
        if isinstance(value, dict):
            return property, self.__handle_dict(property, value)
        
        if isinstance(value, int):
            return property, self.__handle_integer(property, value)
            
        return property, value
    
    def __handle_dict(self, type: str, dict: dict) -> dict:
        result = {}
        for effect, value in dict.items():
            if isinstance(value, int):
                result[effect] = self.__handle_integer(type, value, effect)
            else:
                result[effect] = value
        return result

    def __handle_integer(self, type: str, value, effect: str = ""):
        library = GeneLibrary.get_instance()
        gene = library.find_gene(self.name, type, effect)

        if not gene:
            return value
        
        key = type
        if effect != "":
            key = effect

        return replace_from_key(key, value, gene.min, gene.max, True)

    
    def __handle_color(self, color: dict) -> str:
        red = color.get("red", 0)
        green = color.get("green", 0)
        blue = color.get("blue", 0)

        color_hex = to_hex(red, green, blue)
        color_name = get_closest_color([red, green, blue])

        return color_name+f' ({color_hex})'
    
    def __handle_personality(self, personalities: dict) -> str:
        config = Config.get_instance()
        expression = config.get_personality_expression()
        personality_depth = self.get_property_value("personality_depth", 0)

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
    
    def __handle_develop(self, dict: dict) -> tuple:
        effect, value = next(iter(dict.items()))

        if isinstance(value, int):
            return effect, self.__handle_integer("develop", value, effect)
        
        return effect, value
    
    def __handle_texture(self, textures: dict) -> str:
        # Sort textures
        textures = {texture: value for texture, value in sorted(textures.items(), key=lambda item: item[1], reverse=True)}

        return list(textures.keys())[0]