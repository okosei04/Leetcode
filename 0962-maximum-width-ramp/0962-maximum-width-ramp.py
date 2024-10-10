class Solution:
    """
    First Pass: Build a stack of indices such that the elements at those indices form a decreasing sequence
    Second Pass: Starting from the end of the list, try to "pop" elements from the stack if the current   element is larger than or equal to the element at the top of the stack. This guarantees that we are checking for the maximum width ramp possible between the current index and the one at the top of the stack.
    """
    def maxWidthRamp(self, nums: List[int]) -> int:
        width = 0
        stack = []

        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        for j in range(len(nums)-1, -1 , -1):
            while stack and nums[stack[-1]] <= nums[j]:
                width = max(width, j - stack[-1])
                stack.pop()

        return width

        
        