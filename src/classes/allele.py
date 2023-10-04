# Alleles are found in pairs in loci.
# The dominant of the two alleles decides the value of the locus.
class Allele:
    def __init__(self, id, value) -> None:
        self.id = id
        self.value = value

    def from_sequence(sequence):
        return Allele(value=sequence[0], id=sequence[1])

    def get_id(self):
        return self.id
    
    def get_value(self):
        return self.value
    
    def get_sequence(self):
        return [self.value, self.id]