from src.modules.some_maths import limit_between

def test_limit_between():
    assert limit_between(-1, 0, 10) == 10
    assert limit_between(0, 0, 10) == 0
    assert limit_between(1, 0, 10) == 1
    assert limit_between(2, 0, 10) == 2
    assert limit_between(3, 0, 10) == 3
    assert limit_between(4, 0, 10) == 4
    assert limit_between(5, 0, 10) == 5
    assert limit_between(6, 0, 10) == 6
    assert limit_between(7, 0, 10) == 7
    assert limit_between(8, 0, 10) == 8
    assert limit_between(9, 0, 10) == 9
    assert limit_between(10, 0, 10) == 10
    assert limit_between(11, 0, 10) == 0
    assert limit_between(12, 0, 10) == 1
    assert limit_between(13, 0, 10) == 2
    assert limit_between(14, 0, 10) == 3
    assert limit_between(15, 0, 10) == 4
    assert limit_between(16, 0, 10) == 5
    assert limit_between(17, 0, 10) == 6
    assert limit_between(18, 0, 10) == 7
    assert limit_between(19, 0, 10) == 8
    assert limit_between(20, 0, 10) == 9
    assert limit_between(2000, 0, 0) == 0