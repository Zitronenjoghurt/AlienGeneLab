import json
import os

from .gene import Gene

current_dir = os.path.dirname(os.path.abspath(__file__))
GENE_FILE_PATH = os.path.join(current_dir, '..', 'data', 'genes.json')

class GeneLibrary:
    __instance = None

    def __init__(self) -> None:
        self.library = {}
        with open(GENE_FILE_PATH, 'r') as json_file:
            genes_data = json.load(json_file)
            for gene_data in genes_data:
                gene = Gene.from_dict(gene_data)
                self.library[gene.id] = gene

    def get_instance():
        if GeneLibrary.__instance is None:
            GeneLibrary.__instance = GeneLibrary()
        return GeneLibrary.__instance

    def get_all_genes(self):
        return self.library
    
    def get_all_developing_genes(self):
        filtered_library = {id: gene for id, gene in self.library.items() if gene.type == 'develop'}
        return filtered_library
    
    def get_all_non_developing_genes(self):
        filtered_library = {id: gene for id, gene in self.library.items() if gene.type != 'develop'}
        return filtered_library