from random import choices
from .config import Config
from .gene_library import GeneLibrary
from .haplotype import Haplotype
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
    
    def generate_from_haplotypes(ht1, ht2):
        config = Config.get_instance()
        duplicate_alleles = config.get_setting("duplicate_differing_alleles")
        duplicate_alleles_chance = config.get_setting("duplicate_differing_alleles_chance")

        loci = {}
        overlapping_ids = ht1.get_overlapping_alleles(ht2)
        for id in overlapping_ids:
            loci[id] = Locus(ht1.get_allele(id), ht2.get_allele(id))

        if duplicate_alleles:
            differing_ids = ht1.get_differing_alleles(ht2)
            ht1_ids = set(ht1.get_alleles().keys())
            for id in differing_ids:
                insert = choices([True, False], [duplicate_alleles_chance, 1 - duplicate_alleles_chance])[0]
                if not insert:
                    continue
                if id in ht1_ids:
                    loci[id] = Locus(ht1.get_allele(id), ht1.get_allele(id))
                else:
                    loci[id] = Locus(ht2.get_allele(id), ht2.get_allele(id))

        return Genotype(loci)
    
    def get_locus(self, id):
        return self.loci.get(id, None)

    def get_locus_value(self, id):
        locus = self.get_locus(id)

        if not locus:
            return None
        
        return locus.get_dominant_value()
    
    def get_random_haplotype(self):
        alleles = {}

        for id, locus in self.loci.items():
            alleles[id] = locus.get_random_allele()

        return Haplotype(alleles)