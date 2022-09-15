from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """        

        for left in range(len(nums)):
            if nums[left] != 0:
                continue  

            for right in range(left, len(nums)):
                if nums[right] == 0:
                    continue

                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            
            return
        

            

s = Solution()
nums, moved = [1], [1]
s.moveZeroes(nums)
assert nums == moved

nums, moved = [0], [0]
s.moveZeroes(nums)
assert nums == moved

nums, moved = [0, 1], [1, 0]
s.moveZeroes(nums)
assert nums == moved

nums, moved = [1, 0], [1, 0]
s.moveZeroes(nums)
assert nums == moved

nums, moved = [1, 2], [1, 2]
s.moveZeroes(nums)
assert nums == moved

nums, moved = [1, 2, 0, 3, 4, 0, 0, 0, 7], [1, 2, 3, 4, 7, 0, 0, 0, 0]
s.moveZeroes(nums)
assert nums == moved

nums, moved = [1, 2, 0, 3, 4, 0, 0, 0], [1, 2, 3, 4, 0, 0, 0, 0]
s.moveZeroes(nums)
assert nums == moved

nums, moved = [0,1,0,3,12], [1,3,12,0,0]
s.moveZeroes(nums)
assert nums == moved
