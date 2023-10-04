# The haplotype is the genotype split in half.
# Two haplotypes can be fused back to a genotype.
class Haplotype:
    def __init__(self, alleles = {}) -> None:
        self.alleles = alleles

    def get_overlapping_alleles(self, other_haplotype):
        ids_1 = set(self.alleles.keys())
        ids_2 = set(other_haplotype.get_alleles().keys())

        return ids_1.intersection(ids_2)

    def get_differing_alleles(self, other_haplotype):
        ids_1 = set(self.alleles.keys())
        ids_2 = set(other_haplotype.get_alleles().keys())

        return ids_1 ^ ids_2
    
    def get_alleles(self):
        return self.alleles
    
    def get_allele(self, id):
        return self.alleles.get(id, None)