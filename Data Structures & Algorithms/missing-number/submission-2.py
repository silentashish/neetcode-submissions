class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        high = max(nums)
        nums.sort()

        for i in range(0, high):
            if nums[i] != i:
                return i
        return high + 1 
