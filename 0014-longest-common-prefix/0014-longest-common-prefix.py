class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(min(strs, key=len))):
            for char in strs:
                if char[i] != strs[0][i]:
                    return res
            res+= char[i]

        return res