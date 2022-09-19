from typing import List


def max_num(arr: List[int]) -> int:   
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[0] if arr[0] > max_num(arr[1:]) else max_num(arr[1:])


assert max_num([2, 4, 6, 8, 10, -1, 0]) == 10
assert max_num([1, 1]) == 1
assert max_num([0]) == 0
assert max_num([-1, -111]) == -1