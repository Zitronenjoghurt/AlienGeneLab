from src.modules.genetic_code import encode, decode, to_base4, from_base4

def test_encode():
    assert encode([0, 1, 2, 3, 255]) == 'AAAAAAAGAAACAAATTTTT'

def test_decode():
    assert decode('AAAAAAAGAAACAAATTTTT') == [0, 1, 2, 3, 255]
    assert decode('aAAAxxvbbnAAAg31.;sdAAACAAATTTTT') == [0, 1, 2, 3, 255]