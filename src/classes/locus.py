from random import randint, choice

from .allele import Allele

# A locus (also called gene) decides a certain property of a body part.
# It is made up of two alleles, where the dominant of the two determines the end result.
class Locus:
    def __init__(self, first_allele: Allele, second_allele: Allele) -> None:
        self.first = first_allele
        self.second = second_allele

    # Generate a random locus.
    # pure => if true, both alleles in the locus are the same
    def generate_random(id, min: int, max: int, pure: bool = True) -> 'Locus':
        first_allele = Allele(id, randint(min, max), randint(0, 255))

        if pure:
            second_allele = Allele(id, first_allele.get_value(), first_allele.get_dominance())
        else:
            second_allele = Allele(id, randint(min, max), randint(0, 255))
        
        return Locus(first_allele, second_allele)
    
    def from_sequence(sequence: list) -> 'Locus':
        if sequence[5] != sequence[2]:
            sequence[5] = sequence[2]
        first = Allele.from_sequence([sequence[0], sequence[1], sequence[2]])
        second = Allele.from_sequence([sequence[3], sequence[4], sequence[5]])

        return Locus(first, second)
    
    def get_dominant_value(self) -> int:
        first_value = self.first.get_value()
        second_value = self.second.get_value()

        if self.first.get_dominance() > self.second.get_dominance():
            return first_value
        elif self.first.get_dominance() < self.second.get_dominance():
            return second_value
        else:
            return max(first_value, second_value)
    
    def get_random_allele(self) -> Allele:
        return choice([self.first, self.second])
    
    def get_sequence(self) -> list:
        first = self.first.get_sequence()
        second = self.second.get_sequence()

        return first + second
    
    def get_id(self) -> int:
        return self.first.get_id()
    
    def to_dict(self) -> dict:
        return {"1": self.first.to_dict(), "2": self.second.to_dict()}