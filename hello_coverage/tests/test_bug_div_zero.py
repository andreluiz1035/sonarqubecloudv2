import pytest

def test_bug_div_zero():
    with pytest.raises(ZeroDivisionError):
        import bug_div_zero
