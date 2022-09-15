from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1        

        while left < right:
            res = numbers[left] + numbers[right]            
            if res == target:
                return [left+1, right+1]
            if res > target:
                right -= 1                
            else:
                left += 1

s = Solution()
assert s.twoSum([2,7,11,15], 9) == [1,2]
assert s.twoSum([2,3,4], 6) == [1,3]
assert s.twoSum([-1,0], -1) == [1,2]
assert s.twoSum([5,25,75], 100) == [2,3]



                
                