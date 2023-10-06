import json
from ..modules.part_type_handler import handle_part_type

from .genotype import Genotype
from .phenotype import Phenotype
from .gene_library import GeneLibrary

# An entity which holds a genotype and phenotype.
# The genotype describes how the alien 'looks' on a genetic level.
# The phenotype describes how the alien looks when seen with our own eyes.
class Alien:
    def __init__(self, genotype) -> None:
        self.genotype = genotype
        self.phenotype = Phenotype.generate_from_genotype(genotype)

    def export_to_json(self, filename: str):
        full_info = self.get_full_info()
        with open(filename, 'w') as json_file:
            json.dump(full_info, json_file, indent=4)

    # Generates a random alien.
    # pure => if true, the alien genotype will only have loci with 2 of the same alleles
    def generate_random(pure=True):
        genotype = Genotype.generate_random(pure)
        return Alien(genotype)
    
    def from_genetic_code(code):
        genotype = Genotype.from_genetic_code(code)
        return Alien(genotype)

    def get_genetic_code(self):
        return self.genotype.to_genetic_code()
    
    # Breed this alien with another to create an offspring.
    def breed(self, partner_alien):
        ht1 = self.get_random_haplotype()
        ht2 = partner_alien.get_random_haplotype()

        genotype = Genotype.generate_from_haplotypes(ht1, ht2)
        return Alien(genotype)
    
    def breed_multiple(self, partner_alien, amount):
        aliens = []
        for _ in range(amount):
            aliens.append(self.breed(partner_alien))
        return aliens
    
    # Generates a description dictionary which is a representation of the aliens phenotype, just easier to read.
    def get_description(self) -> dict:
        parts = list(self.get_phenotype_dict().keys())

        description = {}

        # Iterate all parts found in the alien to check their properties.
        for part_name in parts:
            part_info = {}
            part = self.get_part(part_name)
            # Depending on the type of the property, different information will be added to the description.
            for type_name in part:
                value = part[type_name]
                part_info[type_name] = handle_part_type(part, type_name, value)
            description[part_name] = part_info

        return description

    def get_phenotype_dict(self) -> dict:
        return self.phenotype.get_parts()
    
    def get_genotype_dict(self) -> dict:
        return self.genotype.to_dict()
    
    def get_full_info(self) -> dict:
        info = {
            "genetic_code": self.get_genetic_code(),
            "allele_sequence": self.get_allele_sequence(),
            "genotype": self.get_genotype_dict(),
            "phenotype": self.get_phenotype_dict(),
            "description": self.get_description()
        }
        return info
    
    def get_part(self, part) -> dict:
        return self.phenotype.get_part(part)
    
    def get_random_haplotype(self):
        return self.genotype.get_random_haplotype()
    
    def get_allele_sequence(self):
        library = GeneLibrary.get_instance()
        sequence = self.genotype.get_sequence()
        
        alleles = []
        for i in range (0, len(sequence), 2):
            value = sequence[i]
            id = sequence[i+1]
            alleles.append(str(value) + library.get_gene_code(id))
        
        return ''.join(["("+allele+ ")" for allele in alleles])