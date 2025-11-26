from vulneravel import autenticar

def test_autenticar():
    assert autenticar("admin", "123456") == True
    assert autenticar("x", "y") == False
