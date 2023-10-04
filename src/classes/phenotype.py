from .gene_library import GeneLibrary

class Phenotype:
    def __init__(self, parts={}) -> None:
        self.parts = parts

    def generate_from_genotype(genotype):
        library = GeneLibrary.get_instance()

        parts = {}
        for gene in library.get_all_developing_genes().values():
            if genotype.get_locus(gene.id) is not None:
                parts[gene.part] = {}

        existing_parts = list(parts.keys())
        for gene in library.get_all_non_developing_genes().values():
            if gene.part in existing_parts:
                parts.setdefault(gene.part, {}).setdefault(gene.type, {})[gene.effect] = genotype.get_locus_value(gene.id)

        return Phenotype(parts)
    
    def get_parts(self) -> dict:
        return self.parts
    
    def get_part(self, part) -> dict:
        if not self.parts[part]:
            return None
        return self.parts[part]