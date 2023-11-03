from .gene_library import GeneLibrary
from .part import Part

# The phenotype decides how the alien will look like from the outside.
# It transforms the raw information of the genotype for practical use.
class Phenotype:
    def __init__(self, parts={}) -> None:
        self.parts = parts

    def generate_from_genotype(genotype):
        library = GeneLibrary.get_instance()

        parts = {}

        # Iterate all developing genes found in the library and check if they exist in the current genotype.
        # Developing genes decide if a certain part is developed in the alien.
        for gene in library.get_all_developing_genes().values():
            locus = genotype.get_locus(gene.id)
            if locus is not None:
                parts[gene.part] = Part(gene.part, gene.effect, locus.get_dominant_value())

        # Iterate all non-developing genes found in the library and check if they exist in the current genotype.
        # If a certain part is influenced but the developing gene of that part does not exist in the genotype
        # it will not effect the end result.
        existing_parts = list(parts.keys())
        for gene in library.get_all_non_developing_genes().values():
            if gene.part in existing_parts:
                parts[gene.part].add_value(gene.type, gene.effect, genotype.get_locus_value(gene.id))

        # other properties
        genetic_sum = genotype.get_genetic_sum()
        if genetic_sum % 2 == 0:
            parts["body"].add_value("sex", "", "male")
        else:
            parts["body"].add_value("sex", "", "female")

        return Phenotype(parts)
    
    def get_parts(self) -> dict:
        return self.parts
    
    def get_part(self, part) -> Part:
        if not self.parts[part]:
            return None
        return self.parts[part]
    
    def to_dict(self) -> dict:
        result = {}
        for part_name, part in self.parts.items():
            result[part_name] = part.__dict__
        return result