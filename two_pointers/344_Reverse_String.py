from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1 
        
        while left < right:
            if s[left] != s[right]:
                s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return s

s = Solution()
assert s.reverseString(["h","e","l","l","o"]) == ["o","l","l","e","h"]
assert s.reverseString(["H","a","n","n","a","h"]) == ["h","a","n","n","a","H"]