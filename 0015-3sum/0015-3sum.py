class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sum_nums = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left_ptr = i + 1
            right_ptr = len(nums)-1
        
            while left_ptr < right_ptr:
                if nums[i] + nums[left_ptr] + nums[right_ptr] == 0:
                    sum_nums.append([nums[i],nums[left_ptr],nums[right_ptr]])

                    while left_ptr < right_ptr and nums[right_ptr]==nums[right_ptr-1]:
                        right_ptr -= 1
                    while left_ptr < right_ptr and nums[left_ptr]==nums[left_ptr+1]:
                        left_ptr += 1
                    
                    left_ptr +=1
                    right_ptr -=1
                
                elif nums[i] + nums[left_ptr] + nums[right_ptr] > 0:
                    right_ptr -=1
                
                else:
                    left_ptr +=1
             
                
                    
            
        return sum_nums
                
        