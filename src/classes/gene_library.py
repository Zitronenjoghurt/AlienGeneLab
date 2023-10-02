import json
import os

from .gene import Gene

current_dir = os.path.dirname(os.path.abspath(__file__))
GENE_FILE_PATH = os.path.join(current_dir, '..', 'data', 'genes.json')

class GeneLibrary:
    _instance = None
    _library_loaded = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GeneLibrary, cls).__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        if not GeneLibrary._library_loaded:
            self.library = {}
            self.load_from_json(GENE_FILE_PATH)
            GeneLibrary._library_loaded = True

    def load_from_json(self, file_path):
        with open(file_path, 'r') as json_file:
            genes_data = json.load(json_file)
            for gene_data in genes_data:
                gene = Gene.from_dict(gene_data)
                self.library[gene.id] = gene

    def get_all_genes(self):
        return self.library