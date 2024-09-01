class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float("inf")
        windowSum = 0
        ptr = 0
        for i in range(len(nums)):
            windowSum += nums[i]

            while windowSum >= target:
                minLength = min(minLength, i - ptr + 1)
                windowSum -= nums[ptr]
                ptr += 1
        return minLength if minLength!= float("inf") else 0
            

            
