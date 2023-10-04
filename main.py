from src.classes.gene_library import GeneLibrary
from src.classes.alien import Alien

if __name__ == "__main__":
    alien1 = Alien.generate_random()
    alien2 = Alien.generate_random()
    babus = alien1.breed_multiple(alien2, 10)
    desc = [babu.get_description() for babu in babus]
    t = 1