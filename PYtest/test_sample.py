def add(a, b):
    return a + b
def sub(a,b):
     return a-b

def multiply(a,b):
    return a*b

def test_multiply():
    assert multiply(4,5) == 20

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(0, 5) == 0
    assert multiply(-2, 3) == -6


#  this is a failed test case
def test_multiply_fail():
    assert multiply(2,2) == 2
    

def test_add_positive():
    assert add(2, 3) == 5

def test_add_negative():
    assert add(-1, -1) == -2

def test_add_zero():
    assert add(5, 0) == 5

def test_add():
    assert 2 + 3 == 5

def test_sub():
    assert 5 - 2 == 3

def test_sub_negative():
    assert sub(2, 5) == -3


# It  is a failed test case 
def test_fail():
    assert 2 + 2 == 5
