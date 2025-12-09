import pytest

def test_bug_div_zero():
 #   with pytest.raises(ZeroDivisionError):
 #       import bug_div_zero
    try:

        import bug_div_zero

    except ZeroDivisionError:

        assert False   # só entra aqui se ocorrer erro

    else:

        assert True  # se não deu erro, teste falha


        
 