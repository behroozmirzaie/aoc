import pytest 


def solution(locations):
    left = []
    right = []
    locations = locations.split("\n")
    for line in locations: 
        if not line:
            break
        left_value,right_value = line.split()
        left.append(left_value)
        right.append(right_value)
    result = 0 
    for value in left:
        if value in right:
            score = right.count(value)
            result += int(value) * score
    print(f"this is result {result}")
    return result

if __name__ == '__main__':
    with open("input.txt") as f:
        solution(f.read())
