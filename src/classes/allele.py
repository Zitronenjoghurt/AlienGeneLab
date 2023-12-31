from .gene_library import GeneLibrary
from ..modules.some_maths import limit_between

# Alleles are found in pairs in loci.
# The dominant of the two alleles decides the value of the locus.
class Allele:
    def __init__(self, id: int, value: int, dominance: int) -> None:
        self.id = id
        self.value = value
        self.dominance = dominance

    def from_sequence(sequence: list) -> 'Allele':
        library = GeneLibrary.get_instance()

        id = sequence[2]
        id = limit_between(id, 0, library.get_max_id())
        
        gene = library.get_gene(id)

        value = sequence[1]
        value = limit_between(value, gene.min, gene.max)

        dominance = sequence[0]

        return Allele(id, value, dominance)

    def get_id(self) -> int:
        return self.id
    
    def get_value(self) -> int:
        return self.value
    
    def get_dominance(self) -> int:
        return self.dominance
    
    def get_sequence(self) -> list:
        return [self.dominance, self.value, self.id]
    
    def to_dict(self) -> dict:
        return {"id": self.id, "value": self.value, "dominance": self.dominance}