from part_1 import solution
from part_2 import solution as part_2_solution
import pytest


@pytest.mark.parametrize("input_sample,expected", [
    ("xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))", 161)
])
def test_solution(input_sample, expected):
    assert solution(input_sample) == expected


@pytest.mark.parametrize("input_sample,expected", [
    ("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))", 48)
])
def test_solution_part_2(input_sample, expected):
    assert part_2_solution(input_sample) == expected
