import pytest
from typing import List
import re

def solution(file_input):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, file_input)
    result = 0 

    for match  in matches:
        x,y = match.split('(')[-1].split(')')[0].split(',')
        result += int(x) * int(y)
    print(f"this is result: {result}")
    return result


if __name__ == '__main__':
    with open("input.txt") as f:
        solution(f.read())
