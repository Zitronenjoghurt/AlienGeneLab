from random import choices
from .config import Config
from .gene_library import GeneLibrary
from .locus import Locus

class Genotype:
    def __init__(self, loci={}) -> None:
        self.loci = loci

    def generate_random(pure=True):
        config = Config.get_instance()
        library = GeneLibrary.get_instance()
        genes = library.get_all_genes()

        loci = {}
        for id, gene in genes.items():
            insertion_chance = config.get_setting("gene_insertion_chance")
            insert = choices([True, False], [insertion_chance, 1 - insertion_chance])[0]
            if insert:
                loci[id] = Locus.generate_random(id, gene.min, gene.max, pure)
        return Genotype(loci)
    
    def get_locus(self, id):
        return self.loci.get(id, None)

    def get_locus_value(self, id):
        locus = self.get_locus(id)

        if not locus:
            return None
        
        return locus.get_dominant_value()