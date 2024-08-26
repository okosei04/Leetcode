class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        found_zero = False
        for i in range(len(s)):
            if s[i]== "0":
                found_zero = True
            elif s[i] == "1" and found_zero:
                return False
        return True
        