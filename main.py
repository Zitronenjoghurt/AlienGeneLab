from src.classes.gene_library import GeneLibrary
from src.classes.alien import Alien

if __name__ == "__main__":
    alien = Alien.generate_random()
    t = alien.get_description()
    print(t)