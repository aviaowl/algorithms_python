import pytest
from karatsuba_muliplication_algorithm import Solution


@pytest.mark.parametrize("x,y,answer", [
    ('1234', '5678', '7006652'),
    ('2925', '6872', '20100600'),
    ('1', '2', '2'),
    ('123', '456', '56088'),
    ('123', '12', '1476'),
    ('12345678910111213141516', '16151413121110987654321', '199400160337793445446342635587252530261890636')
])
def test_multiply(x: str, y: str, answer: int):
    sol = Solution()
    actual = sol.multiply(x, y)
    assert actual == answer