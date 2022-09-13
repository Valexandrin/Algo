def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:        
        right = n
        left = 0

        while right - left > 1:
            step = left + (right - left) // 2
            if isBadVersion(step):
                right = step                
            else:
                left = step        

        return right