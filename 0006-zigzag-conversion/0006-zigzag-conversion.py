class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        res = ""

        for r in range(numRows):
            increement = 2 * (numRows- 1)
            for c in range(r, len(s), increement):
                res += s[c]
                
                if (r > 0 and r < numRows-1 and c + increement -2 *r < len(s)):
                    res += s[c + increement -2 * r]

        return res  