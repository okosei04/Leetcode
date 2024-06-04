class Solution:
    def isPalindrome(self, x: int) -> bool:
        k = str(x)
        return str(x) == k[::-1]
        