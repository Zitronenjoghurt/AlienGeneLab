from copy import deepcopy
from random import randint, choice

from .allele import Allele

# A locus (also called gene) decides a certain property of a body part.
# It is made up of two alleles, where the dominant of the two determines the end result.
class Locus:
    def __init__(self, first_allele, second_allele) -> None:
        self.first = first_allele
        self.second = second_allele

    # Generate a random locus.
    # pure => if true, both alleles in the locus are the same
    def generate_random(id, min, max, pure=True):
        first_allele = Allele(id, randint(min, max))
        second_allele = deepcopy(first_allele)

        if not pure:
            second_allele = Allele(id, randint(min, max))
        
        return Locus(first_allele, second_allele)
    
    def get_dominant_value(self):
        first_value = self.first.get_value()
        second_value = self.second.get_value()

        return max(first_value, second_value)
    
    def get_random_allele(self):
        return choice([self.first, self.second])