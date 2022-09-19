from typing import List

def max_min(arr: List[int]) -> List[int]:
    if len(arr) < 2:
        return False    
    mn, mx = arr[0], arr[0]
    for i in range(1, len(arr)):
        if mn > arr[i]:
            mn = arr[i]
            continue
        if mx < arr[i]:
            mx = arr[i]        
    
    return [mn, mx]


assert max_min([-1,2]) == [-1,2]
assert max_min([2,-1]) != [2,-1]
assert max_min([20,-1,3,-5]) == [-5,20]
assert max_min([2,2]) == [2,2]
assert max_min([4]) == False, RecursionError