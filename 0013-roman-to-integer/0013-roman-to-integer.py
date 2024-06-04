class Solution:
    def romanToInt(self, s: str) -> int:
        rom_map = {"I":1, "V":  5, "X": 10, "L": 50, "C": 100, "D": 500,"M":1000}
        res = 0
        for i in range(len(s)):
            if i+1 < len(s) and rom_map[s[i]] < rom_map[s[i+1]]:
                res -= rom_map[s[i]]
            else:
                res += rom_map[s[i]]


        return res