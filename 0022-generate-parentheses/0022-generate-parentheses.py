class Solution:
    """
    If n is 1 the output is ()
    If n is 2 the output is ()(), (())
    n = 3  ()()(), ((())), (())(),()(())
    # If the current string has all pairs, add to results
    # If we can add an open parenthesis, add it
    # If we can add a close parenthesis, add it

     """
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def back(currStr, openB, closeB):
            if len(currStr) == 2 * n:
                res.append(currStr)
            
            if openB < n:
                back(currStr + "(", openB + 1, closeB)
            
            if closeB < openB:
                back(currStr + ")", openB, closeB + 1)
        
        back("", 0, 0)
        return res