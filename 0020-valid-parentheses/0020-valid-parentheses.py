class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = "([{"
        brackets = {"(":")", "{":"}", "[":"]"}
        stack = []
        for char in s:
            if char in open_brackets:
                stack.append(char)
            
            elif stack and char == brackets[stack[-1]]:
                stack.pop()
                
            else:
                return False
        
        return not stack
        