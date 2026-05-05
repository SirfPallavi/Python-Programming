# import pytest

# @pytest.mark.parametrize("a, b, result", [
#     (2, 3, 5),
#     (4, 5, 9),
#     (1, 1, 2)
# ])
# def test_add(a, b, result):
#     assert a + b == result


import pytest

def multiply(a, b):
    return a * b

@pytest.mark.parametrize("a, b, result", [
    (2, 3, 6),
    (2,3,5),  
    # This will fail
    (5, 0, 0),
    (-2, 3, -6)
])
def test_multiply(a, b, result):
    assert multiply(a, b) == result

