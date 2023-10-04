from ..modules.part_type_handler import handle_part_type

from .genotype import Genotype
from .phenotype import Phenotype

class Alien:
    def __init__(self, genotype) -> None:
        self.genotype = genotype
        self.phenotype = Phenotype.generate_from_genotype(genotype)

    def generate_random(pure=True):
        genotype = Genotype.generate_random(pure)
        return Alien(genotype)
    
    def breed(self, partner_alien):
        ht1 = self.get_random_haplotype()
        ht2 = partner_alien.get_random_haplotype()

        genotype = Genotype.generate_from_haplotypes(ht1, ht2)
        return Alien(genotype)
    
    def get_description(self) -> dict:
        parts = list(self.get_parts().keys())

        description = {}
        for part_name in parts:
            part_info = {}
            part = self.get_part(part_name)
            for type_name in part:
                value = part[type_name]
                part_info[type_name] = handle_part_type(part_name, type_name, value)
            description[part_name] = part_info

        return description

    def get_parts(self) -> dict:
        return self.phenotype.get_parts()
    
    def get_part(self, part) -> dict:
        return self.phenotype.get_part(part)
    
    def get_random_haplotype(self):
        return self.genotype.get_random_haplotype()