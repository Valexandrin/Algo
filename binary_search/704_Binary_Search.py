from typing import List

def search(nums: List[int], target: int) -> int:
    mid = len(nums)//2
    
    if len(nums) == 1:
        if nums[mid] == target:
            return mid                
        return -1
    if nums[mid] == target:
        return mid

    if target < nums[mid]:
        get_next = search(nums[:mid], target)
        if get_next >= 0:
            return get_next 
        return get_next
    
    get_next = search(nums[mid:], target)
    if get_next >= 0:
        return mid + get_next 
    return get_next
    
        

test_list = [
    ([-1,0,3,5,9,12], 9),
    ([-1,0,3,5,9,12], 2),
    ([-1,0,3,5,9,12], -1),
    ([2,5], 2),
]

for nums, target in test_list:
    print(search(nums, target))
