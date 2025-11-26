from duplicado import soma, soma_numeros

def test_soma():
    assert soma(2, 3) == 5

def test_soma_numeros():
    assert soma_numeros(4, 6) == 10
