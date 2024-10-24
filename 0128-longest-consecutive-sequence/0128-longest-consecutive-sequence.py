class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        - Use a hash set to store the numbers for O(1) lookups.
        - For each number, check if it's the start of a sequence by ensuring num - 1 is not in the set
        - If it's the start, count the length of the consecutive sequence by checking num + 1, num + 2, etc.
        - Track and return the longest sequence found.
        """
        numSet = set(nums)
        longestSequence = 0

        for n in numSet:
            if n - 1 not in  numSet:
                currSmallest = n
                currMax = 1

                while currSmallest + 1 in numSet:
                    currMax += 1
                    currSmallest += 1
            
                longestSequence = max(longestSequence, currMax)

        return longestSequence
            