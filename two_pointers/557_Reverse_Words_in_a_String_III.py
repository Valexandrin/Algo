class Solution:
    def reverseWords(self, s: str) -> str:
        L = s.split(' ')
        return ' '.join([word[len(word)-1::-1] for word in L])

s = Solution()
assert s.reverseWords("Let's take LeetCode contest") == "s'teL ekat edoCteeL tsetnoc"
