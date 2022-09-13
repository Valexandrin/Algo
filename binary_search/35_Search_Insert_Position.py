from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums)-1        

        while start < end:
            mid = start + (end - start)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                start = mid + 1
            else:
                end = mid
        
        if nums[end] > target:
            return end
        return end + 1

    
        

test_list = [
    ([-1,0,3,5,9,12], 9),
    ([-1,0,3,5,9,12], 4),
    ([-1,0,3,5,9,12], 1),
    ([2,5], 12),
    ([1,3,5,6], -1),
]

s = Solution()
for nums, target in test_list:
    print(s.searchInsert(nums, target))