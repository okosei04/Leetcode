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

        def bactrack(curr_str, open_brac, close_brac):
            if len(curr_str) == 2 * n:
                res.append(curr_str)
                

            if open_brac < n:
                bactrack(curr_str + "(", open_brac + 1, close_brac)

            if close_brac < open_brac:
                bactrack(curr_str + ")", open_brac, close_brac + 1)

        bactrack("", 0, 0)

        return res

            




        