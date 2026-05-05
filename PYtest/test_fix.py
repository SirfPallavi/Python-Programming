import pytest

# # @pytest.fixture
# # def numbers():
# #     return (2, 3)

# # def multiply(a, b):
# #     return a * b

# # def test_multiply(numbers):
# #     a, b = numbers
# #     assert multiply(a, b) == 6

# Why we use fixtures ??

# 👉 Reusability
# 👉 Clean code
# 👉 Same data multiple tests me use


@pytest.fixture
def num():
    return 5

def test_square(num):
    assert num * num == 25

def test_double(num):
    assert num * 2 == 10
#  👉 we can use same fixtures data multiple test
