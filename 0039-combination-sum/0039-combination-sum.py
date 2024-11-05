class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
    
        def possibleCom(ans, currIndex, currSum):

            if currSum == target:
                res.append(ans[:])
                return
            
            if currSum > target:
                return


            
            for i in range(currIndex, len(candidates)):
                ans.append(candidates[i])
                possibleCom(ans, i, currSum + candidates[i])
                ans.pop()

        possibleCom([], 0, 0)
        return res
        