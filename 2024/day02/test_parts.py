from part_1 import solution
from part_2 import solution as part_2_solution
import pytest


@pytest.mark.parametrize("input_sample,expected", [
    ("""7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""", 2)
])
def test_solution(input_sample, expected):
    assert solution(input_sample) == expected


@pytest.mark.parametrize("input_sample,expected", [
    ("""7 6 4 2 1
    1 2 7 8 9
    9 7 6 2 1
    1 3 2 4 5
    8 6 4 4 1
    1 3 6 7 9""", 4)
])
def test_solution_part_2(input_sample, expected):
    assert part_2_solution(input_sample) == expected
