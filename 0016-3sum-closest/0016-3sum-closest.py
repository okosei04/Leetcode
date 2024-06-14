class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        
        for i in range(len(nums)-2):
            right_ptr, left_ptr = len(nums)-1,  i + 1
            while left_ptr < right_ptr:
                sumNums = nums[left_ptr] + nums[right_ptr] + nums[i]
                if abs(sumNums-target) < abs(res-target):
                    res = sumNums
                if sumNums < target:
                    left_ptr+=1
                elif sumNums > target:
                    right_ptr-=1
                else:
                    return target
        return res        