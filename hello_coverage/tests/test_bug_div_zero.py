import pytest

def test_bug_div_zero():
 #   with pytest.raises(ZeroDivisionError):
 #       import bug_div_zero
#    try:

 #       import bug_div_zero

  #  except ZeroDivisionError:

   #     assert True   # só entra aqui se ocorrer erro

    #else:

     #   assert False  # se não deu erro, teste falha
 
 Result = False

 try:

        import bug_div_zero

 except ZeroDivisionError:

        Result =  True   # só entra aqui se ocorrer erro

 
 assert Result  # se não deu erro, teste falha
 