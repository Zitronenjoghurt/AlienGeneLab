from src.classes.gene_library import GeneLibrary
from src.classes.alien import Alien

if __name__ == "__main__":
    alien1 = Alien.generate_random()
    code = alien1.get_genetic_code()
    alien2 = Alien.from_genetic_code(code)

    print(alien1.get_description())
    print(alien1.get_genetic_code())
    print(alien2.get_description())
    print(alien2.get_genetic_code())
    t = 1