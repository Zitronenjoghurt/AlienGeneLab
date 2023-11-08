from src.modules.genetic_code import encode, decode, to_base4, from_base4, flip_char

def test_encode():
    assert encode([0, 1, 2, 3, 255]) == 'AAAAAAAGAAACAAATTTTT'

def test_decode():
    assert decode('AAAAAAAGAAACAAATTTTT') == [0, 1, 2, 3, 255]
    assert decode('aAAAxxvbbnAAAg31.;sdAAACAAATTTTT') == [0, 1, 2, 3, 255]

def test_to_base4():
    assert to_base4(0) == 'AAAA'
    assert to_base4(1) == 'AAAG'
    assert to_base4(2) == 'AAAC'
    assert to_base4(3) == 'AAAT'
    assert to_base4(4) == 'AAGA'
    assert to_base4(5) == 'AAGG'
    assert to_base4(6) == 'AAGC'
    assert to_base4(7) == 'AAGT'
    assert to_base4(8) == 'AACA'
    assert to_base4(9) == 'AACG'
    assert to_base4(10) == 'AACC'
    assert to_base4(11) == 'AACT'
    assert to_base4(12) == 'AATA'
    assert to_base4(13) == 'AATG'
    assert to_base4(14) == 'AATC'
    assert to_base4(15) == 'AATT'
    assert to_base4(16) == 'AGAA'
    assert to_base4(255) == 'TTTT'

def test_flip_char():
    for _ in range (10000):
        a = flip_char('A')
        g = flip_char('G')
        t = flip_char('T')
        c = flip_char('C')

        assert a != 'A'
        assert g != 'G'
        assert t != 'T'
        assert c != 'C'

        assert a in ['G', 'T', 'C']
        assert g in ['A', 'T', 'C']
        assert t in ['A', 'G', 'C']
        assert c in ['A', 'G', 'T']