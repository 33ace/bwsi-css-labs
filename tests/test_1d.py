from lab_1d import two_sum

def test_d_basic():
    assert two_sum([3, 1, 4], 7) == [0, 2]

def test_d_big_numbers():
    assert two_sum([10, 20, 30, 40], 70) == [2, 3]
    