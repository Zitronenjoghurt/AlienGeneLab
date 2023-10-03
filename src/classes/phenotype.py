from .gene_library import GeneLibrary

class Phenotype:
    def __init__(self, parts={}) -> None:
        self.parts = parts

    def generate_from_genotype(genotype):
        library = GeneLibrary().get_all_genes()

        parts = {}
        for gene in library.values():
            value = genotype.get_locus_value(gene.id)

            if value is not None:
                parts.setdefault(gene.part, {}).setdefault(gene.type, {})[gene.effect] = genotype.get_locus_value(gene.id)

        return Phenotype(parts)
    
    def get_parts(self) -> dict:
        return self.parts
    
    def get_part(self, part) -> dict:
        if not self.parts[part]:
            return None
        return self.parts[part]