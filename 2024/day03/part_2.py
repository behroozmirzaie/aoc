import pytest
from typing import List
import re

def solution(file_input):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, file_input)
    result = 0 
    enable = True
    for match  in matches:
        if match == 'do()':
           enable = True
        elif match == "don't()":
            enable = False
        else:
            if enable: 
                x,y = match.split('(')[-1].split(')')[0].split(',')
                result += int(x) * int(y)
    print(f"this is result: {result}")
    return result


if __name__ == '__main__':
    with open("input.txt") as f:
        solution(f.read())
