from .gene_library import GeneLibrary
from .locus import Locus

class Genotype:
    def __init__(self, loci={}) -> None:
        self.loci = loci

    def generate_random(pure=True):
        library = GeneLibrary().get_all_genes()

        loci = {}
        for id, gene in library.items():
            loci[id] = Locus.generate_random(id, gene.min, gene.max, pure)
        return Genotype(loci)
    
    def get_locus(self, id):
        return self.loci.get(id, None)

    def get_locus_value(self, id):
        locus = self.get_locus(id)

        if not locus:
            return None
        
        return locus.get_dominant_value()