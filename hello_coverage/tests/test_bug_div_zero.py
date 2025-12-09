import sys
import importlib
 
def test_bug_div_zero():
    if "bug_div_zero" in sys.modules:
        del sys.modules["bug_div_zero"]
 
    Result = True
    try:
        importlib.import_module("bug_div_zero")
    except ZeroDivisionError:
        Result = False
 
    assert Result

