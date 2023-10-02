from .gene_library import GeneLibrary

class Phenotype:
    def __init__(self, parts={}) -> None:
        self.parts = parts

    def generate_from_genotype(genotype):
        library = GeneLibrary().get_all_genes()

        parts = {}
        for gene in library.values():
            parts.setdefault(gene.part, {}).setdefault(gene.type, {})[gene.effects] = genotype.get_locus_value(gene.id)

        return Phenotype(parts)