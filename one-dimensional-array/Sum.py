from typing import List


def summ(arr: List[int]) -> int:   
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] + summ(arr[1:])


assert summ([-2, 4, 6, -8, 10]) == 10
assert summ([3]) == 3
assert summ([0, 0]) == 0
