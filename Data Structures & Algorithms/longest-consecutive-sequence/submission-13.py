class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
            
        nums = sorted(nums)
        
        max_count = 1
        count = 1

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            elif nums[i] == nums[i-1]:
                continue
            else:
                max_count = max(max_count, count)
                count = 1
        
        return max(count,max_count)
        