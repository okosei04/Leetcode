class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        words = sentence.split()
        # firstLast = curr = breakWord[0][-1] 
        
        n = len(words)
        for i in range(n):
            if words[i][-1] != words[(i+1)%n][0]:
                return False
        return True
        