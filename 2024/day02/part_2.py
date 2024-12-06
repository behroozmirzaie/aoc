import pytest
from typing import List


def solution(file_input):
    result = 0
    input_list = file_input.split("\n")
    for line in input_list:
        cleaned_line = line.split()
        numbers = [int(x) for x in cleaned_line]
        if _validate_safe_line(numbers):
            result += 1
        else:
            for i in range(len(numbers)):
                new_numbers = numbers[:i] + numbers[i + 1:]
                if _validate_safe_line(new_numbers):
                    result += 1
                    break
    print(f"this is result {result}")
    return result


def _validate_safe_line(numbers: List[int]) -> bool:
    if not numbers:
        return False
    if numbers[0] > numbers[1]:
        direction = -1
    else:
        direction = 1
    for i, j in zip(numbers, numbers[1:]):
        dif = direction * (j - i)
        if 1 <= dif <= 3:
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    with open("input.txt") as f:
        solution(f.read())
