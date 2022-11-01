from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:        
        res = []

        def add_bracket(left, right, sub = ''):
            if not left and not right:
                res.append(sub)            
            if left:                    
                add_bracket(left-1, right, sub+'(')
            if left < right:
                add_bracket(left, right-1, sub+')')
        
        add_bracket(n, n)
        return res

s = Solution()
print(s.generateParenthesis(3))

            
