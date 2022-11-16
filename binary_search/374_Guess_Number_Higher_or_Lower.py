# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    pass

class Solution:
    def guessNumber(self, n: int) -> int:        
        ans, step = n // 2     
        while guess(ans):
            step = step // 2
            if not step:
                step = 1
            ans = ans - step if guess(ans) < 0 else ans + step           
        
        return ans