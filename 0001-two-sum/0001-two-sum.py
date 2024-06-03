class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumNums = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in sumNums:
                return [sumNums[diff], i]
            
            sumNums[v] = i
            
    
        