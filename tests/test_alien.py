from src.classes.alien import Alien

def test_cloning():
    alien = Alien.generate_random()
    code = alien.get_genetic_code()
    clone = Alien.from_genetic_code(code)
    assert alien.get_genotype_dict() == clone.get_genotype_dict()
    assert alien.get_phenotype_dict() == clone.get_phenotype_dict()
    assert alien.get_description() == clone.get_description()