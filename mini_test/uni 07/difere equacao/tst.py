def subtrai_polinomios(p1, p2):
    return p1, p2

def test_exemplo_1(p1, p2):
    p1 = [-5, 4, 3]
    p2 = [-1, 0, 2, 0, 0, 0, 5]
    assert subtrai_polinomios(p1, p2) == [-4, 4, 1, 0, 0, 0, -5]

def test_exemplo_2(p1, p2):
    p1 = [-5, 4, 3]  # 3x2 + 4x - 5
    p2 = [-4, 2, 3]  # 3x2 + 2x - 4
    assert subtrai_polinomios(p1, p2) == [-1, 2]  # 2x - 1