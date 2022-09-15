from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1        
        res = [None]*len(nums)
        ind = right

        l_sq = nums[left]**2
        r_sq = nums[right]**2

        while left < right:
            if l_sq > r_sq:
                res[ind] = l_sq
                left += 1
                l_sq = nums[left]**2
            else:
                res[ind] = r_sq
                right -= 1
                r_sq = nums[right]**2
            ind -= 1
        
        res[ind] = l_sq

        return res
        


s = Solution()
assert s.sortedSquares([-4,-1,0,3,10]) == [0,1,9,16,100]
assert s.sortedSquares([-7,-3,2,3,11]) == [4,9,9,49,121]
assert s.sortedSquares([1,2,3,5,11]) == [1,4,9,25,121]
assert s.sortedSquares([1]) == [1]
assert s.sortedSquares([1,1]) == [1,1]
assert s.sortedSquares([-7,-3]) == [9,49]
assert s.sortedSquares([-10000,-9999,-7,-5,0,0,10000]) == [0,0,25,49,99980001,100000000,100000000]

