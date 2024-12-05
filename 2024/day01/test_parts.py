from part_1 import solution
from part_2 import solution as part_2_solution
import pytest




@pytest.mark.parametrize("input_sample,expected",[
    ("3   4\n4   3\n2   5\n1   3\n3   9\n3   3",11)
])
def test_solution(input_sample,expected):
    assert solution(input_sample) == expected





@pytest.mark.parametrize("input_sample,expected",[
    ("3   4\n4   3\n2   5\n1   3\n3   9\n3   3",31)
])
def test_solution_part_2(input_sample,expected):
    assert part_2_solution(input_sample) == expected