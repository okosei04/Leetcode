class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        """
        1. Identify the farthest occurrence of the maximum element.
        2. Identify the nearest occurrence of the minimum element.
        3. Calculate swaps needed to move:
        - Maximum element to the end.
        - Minimum element to the beginning.
        4. Adjust for overlap if the minimum is positioned after the maximum.
        5. Return the total swaps.
        """

        max_element = max(nums)
        min_element = min(nums)
        

        minIndex = maxIndex = 0
       

        for i in range(len(nums)):
            if nums[i] == min_element:
                minIndex = i
                break
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == max_element:
                maxIndex = i
                break

        res = len(nums) - 1 - maxIndex + minIndex


        if minIndex > maxIndex:
            res -= 1
        
        return res

        