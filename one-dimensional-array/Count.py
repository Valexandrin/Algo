def count_length(arr: list) -> int:   
    if arr == []:
        return 0
    else:
        return 1 + count_length(arr[1:])

assert count_length([2, 4, 6, 8, 10]) == 5
assert count_length([]) == 0
assert count_length([-1, -5, 3]) == 3
assert count_length([-1, -5, 3]) != 2
