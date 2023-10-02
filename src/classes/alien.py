from .genotype import Genotype
from .phenotype import Phenotype

class Alien:
    def __init__(self, genotype) -> None:
        self.genotype = genotype
        self.phenotype = Phenotype.generate_from_genotype(genotype)

    def generate_random(pure=True):
        genotype = Genotype.generate_random(pure)
        return Alien(genotype)