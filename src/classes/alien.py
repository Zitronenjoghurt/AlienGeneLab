from ..modules.color import to_hex, get_closest_color

from .genotype import Genotype
from .phenotype import Phenotype

class Alien:
    def __init__(self, genotype) -> None:
        self.genotype = genotype
        self.phenotype = Phenotype.generate_from_genotype(genotype)

    def generate_random(pure=True):
        genotype = Genotype.generate_random(pure)
        return Alien(genotype)
    
    def get_description(self) -> dict:
        parts = list(self.get_parts().keys())

        description = {}
        for part_name in parts:
            part_info = {}
            part = self.get_part(part_name)
            for type in part:
                value = part[type]
                part_info[type] = self.handle_part_type(part, type, value)
            description[part_name] = part_info

        return description

    def handle_part_type(self, part, type, value) -> str:
        if type == "color":
            return get_closest_color(to_hex(value["red"], value["green"], value["blue"]))
        
        return None

    def get_parts(self) -> dict:
        return self.phenotype.get_parts()
    
    def get_part(self, part) -> dict:
        return self.phenotype.get_part(part)
    
    def get_part_color(self, part) -> str:
        part_data = self.get_part(part)
        if not part_color:
            return None
        
        part_color = part_data["color"]
        hex = to_hex(part_color["red"], part_color["green"], part_color["blue"])

        return get_closest_color(hex)