from random import choices
from .config import Config
from .gene_library import GeneLibrary
from .haplotype import Haplotype
from .locus import Locus

from ..modules.genetic_code import decode, encode

# The genotype of an alien is made up of multiple loci,
# where each locus decides a different property of a body part.
class Genotype:
    def __init__(self, loci={}) -> None:
        self.loci = loci

    # Generates a random genotype used to create an alien.
    # pure => if true, the generated genotype will only have loci with 2 of the same alleles
    def generate_random(pure=True):
        config = Config.get_instance()
        library = GeneLibrary.get_instance()
        genes = library.get_all_genes()

        loci = {}

        # Iterates all genes found in the gene library and randomly adds them with random values.
        for id, gene in genes.items():
            insertion_chance = config.get_setting("gene_insertion_chance")
            insert = choices([True, False], [insertion_chance, 1 - insertion_chance])[0]
            if insert:
                loci[id] = Locus.generate_random(id, gene.min, gene.max, pure)
        return Genotype(loci)
    
    # Fuses two haplotypes (one from each parent) and fuses them to a new genotype.
    def generate_from_haplotypes(ht1, ht2):
        config = Config.get_instance()
        duplicate_alleles = config.get_setting("duplicate_differing_alleles")
        duplicate_alleles_chance = config.get_setting("duplicate_differing_alleles_chance")

        loci = {}

        # Fuse the two alleles (if found in both parents) to a locus.
        overlapping_ids = ht1.get_overlapping_alleles(ht2)
        for id in overlapping_ids:
            loci[id] = Locus(ht1.get_allele(id), ht2.get_allele(id))

        # If only one of the two parents has an allele, it has to be duplicated to make up a pair.
        # Depending on the configuration, that duplication may or may not occur at random.
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
    
    def from_sequence(sequence):
        loci = {}
        for i in range(0, len(sequence), 4):
            locus = Locus.from_sequence(sequence[i:i+4])
            id = locus.get_id()
            loci[id] = locus

        return Genotype(loci)

    def from_genetic_code(code):
        sequence = decode(code)

        return Genotype.from_sequence(sequence)

    def to_genetic_code(self):
        sequence = self.get_sequence()

        return encode(sequence)

    def get_locus(self, id):
        return self.loci.get(id, None)

    def get_locus_value(self, id):
        locus = self.get_locus(id)

        if not locus:
            return 0
        
        return locus.get_dominant_value()
    
    # Splits the allele pairs inside every loci of the genotype into a sequence of just alleles.
    def get_random_haplotype(self):
        alleles = {}

        for id, locus in self.loci.items():
            alleles[id] = locus.get_random_allele()

        return Haplotype(alleles)
    
    def get_sequence(self):
        sequence = []

        for locus in self.loci.values():
            sequence.extend(locus.get_sequence())

        return sequence