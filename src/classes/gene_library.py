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
            for id, gene_data in enumerate(genes_data):
                gene = Gene.from_dict(id, gene_data)
                self.library[id] = gene

    def get_instance() -> 'GeneLibrary':
        if GeneLibrary.__instance is None:
            GeneLibrary.__instance = GeneLibrary()
        return GeneLibrary.__instance
    
    def get_gene(self, id: int) -> Gene:
        return self.library.get(id, None)
    
    def find_gene(self, part: str, type: str, effect: str) -> Gene|None:
        results = [entry for entry in self.library.values() if entry.part == part and entry.type == type and entry.effect == effect]

        if len(results) == 0:
            return None
        
        return results[0]
    
    def find_gene_without_type(self, part: str, effect: str) -> Gene|None:
        results = [entry for entry in self.library.values() if entry.part == part and entry.effect == effect]

        if len(results) == 0:
            return None
        
        return results[0]
    
    def get_gene_code(self, id: int) -> str:
        gene = self.get_gene(id)

        if not gene:
            return None
        
        return gene.code

    def get_all_genes(self) -> dict:
        return self.library
    
    def get_all_developing_genes(self) -> dict:
        filtered_library = {id: gene for id, gene in self.library.items() if gene.type == 'develop'}
        return filtered_library
    
    def get_all_non_developing_genes(self) -> dict:
        filtered_library = {id: gene for id, gene in self.library.items() if gene.type != 'develop'}
        return filtered_library
    
    def get_max_id(self) -> int:
        return len(self.library) - 1
    
    def get_overview(self) -> dict:
        overview = {}
        for gene in self.library.values():
            if gene.part not in overview:
                overview[gene.part] = {}
            
            if gene.type not in overview[gene.part]:
                overview[gene.part][gene.type] = []
            
            overview[gene.part][gene.type].append(gene.effect)
        
        return overview