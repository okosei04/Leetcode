class Solution:
    def findLHS(self, nums: List[int]) -> int:
        """
        Check if the number coming affects the criteria given
        in the question and if it does no not include that
        number

        """ 
        maxSequence = 0
        count  = Counter(nums)

        # for num in nums:
        #     if num not in count:
        #         count[num] = 1

        #     else:
        #         count[num] += 1
        

        for n in count:
            if n + 1 in count:
                subsequence = count[n] + count[n+1]
                maxSequence = max(subsequence, maxSequence)

        return maxSequence
            
