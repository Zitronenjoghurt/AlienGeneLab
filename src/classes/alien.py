from ..modules.part_type_handler import handle_part_type

from .genotype import Genotype
from .phenotype import Phenotype

# An entity which holds a genotype and phenotype.
# The genotype describes how the alien 'looks' on a genetic level.
# The phenotype describes how the alien looks when seen with our own eyes.
class Alien:
    def __init__(self, genotype) -> None:
        self.genotype = genotype
        self.phenotype = Phenotype.generate_from_genotype(genotype)

    # Generates a random alien.
    # pure => if true, the alien genotype will only have loci with 2 of the same alleles
    def generate_random(pure=True):
        genotype = Genotype.generate_random(pure)
        return Alien(genotype)
    
    # Breed this alien with another to create an offspring.
    def breed(self, partner_alien):
        ht1 = self.get_random_haplotype()
        ht2 = partner_alien.get_random_haplotype()

        genotype = Genotype.generate_from_haplotypes(ht1, ht2)
        return Alien(genotype)
    
    # Generates a description dictionary which is a representation of the aliens phenotype, just easier to read.
    def get_description(self) -> dict:
        parts = list(self.get_parts().keys())

        description = {}

        # Iterate all parts found in the alien to check their properties.
        for part_name in parts:
            part_info = {}
            part = self.get_part(part_name)
            # Depending on the type of the property, different information will be added to the description.
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