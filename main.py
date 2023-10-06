from src.classes.gene_library import GeneLibrary
from src.classes.alien import Alien

if __name__ == "__main__":
    alien1 = Alien.generate_random()
    alien1.export_to_json('alien.json')