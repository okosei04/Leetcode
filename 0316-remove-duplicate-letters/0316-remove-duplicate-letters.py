class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        Keep track of the last occurence of each char
        Use a stack to store the final characters
        Use a set to skip duplicates
        Check the top of our  stack if the the top of the stack 
        is greater than the curr char and still can appear
        later in the string
        """
        last_occurence = {char:i for i, char in enumerate(s)}
        visited = set()
        stack = []

        for i, char in enumerate(s):
            if char in visited:
                continue
            
            while stack and stack[-1] > char and last_occurence[stack[-1]] > i:
                visited.remove(stack.pop())
            
            stack.append(char)
            visited.add(char)

        return "".join(stack)
        