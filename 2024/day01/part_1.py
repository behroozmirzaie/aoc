import pytest 


def solution(locations):
    left = []
    right = []
    locations = locations.split("\n")
    for line in locations: 
        left_value,right_value = line.split()
        left.append(left_value)
        right.append(right_value)
    left.sort()
    right.sort()
    result = 0 
    for l,r in zip(left,right):
        result += abs(int(l)-int(r))
    print(f"this is result {result}")
    return result

if __name__ == '__main__':
    solution()