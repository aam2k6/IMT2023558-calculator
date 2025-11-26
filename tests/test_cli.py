from calculator import cli

def test_add():
    assert cli.add(2,3)==5

def test_div_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        cli.div(1,0)
