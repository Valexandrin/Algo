from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        end = len(nums) - 1
        
        self.reverse(nums, 0, end)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, end)      

        return nums  

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    

s = Solution()

assert s.rotate([1], 0) == [1]
assert s.rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
assert s.rotate([-1,-100,3,99], 2) == [3,99,-1,-100]
