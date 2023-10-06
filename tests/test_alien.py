from src.classes.alien import Alien

def test_cloning():
    alien = Alien.generate_random()
    code = alien.get_genetic_code()
    clone = Alien.from_genetic_code(code)
    assert alien.get_full_info() == clone.get_full_info()