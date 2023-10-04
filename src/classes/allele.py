from .gene_library import GeneLibrary
from ..modules.some_maths import limit_between

# Alleles are found in pairs in loci.
# The dominant of the two alleles decides the value of the locus.
class Allele:
    def __init__(self, id, value) -> None:
        self.id = id
        self.value = value

    def from_sequence(sequence):
        library = GeneLibrary.get_instance()

        id = sequence[1]
        id = limit_between(id, 1, library.get_max_id())
        
        gene = library.get_gene(id)

        value = sequence[0]
        value = limit_between(value, gene.min, gene.max)

        return Allele(id, value)

    def get_id(self):
        return self.id
    
    def get_value(self):
        return self.value
    
    def get_sequence(self):
        return [self.value, self.id]