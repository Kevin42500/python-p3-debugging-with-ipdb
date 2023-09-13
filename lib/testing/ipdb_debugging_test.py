from lib import ipdb_debugging

def test_adds_two():
    result = ipdb_debugging.plus_two(3)
    assert result == 5
