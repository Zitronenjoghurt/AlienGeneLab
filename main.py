from src.classes.gene_library import GeneLibrary
from src.classes.alien import Alien

if __name__ == "__main__":
    alien1 = Alien.generate_random()
    alien2 = Alien.generate_random()
    babu = alien1.breed(alien2)
    
    c1 = alien1.get_description()
    c2 = alien2.get_description()
    c3 = babu.get_description()

    t = 1