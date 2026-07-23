import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)

            suffix = [1] * n
            prefix = [1] * n
            result = [1] * n

            for i in range(1, n):
                suffix[i] = suffix[i-1]* nums[i-1]
            
            for i in range(n-2, -1, -1):
                prefix[i] = prefix[i+1] * nums[i+1]

            for i in range(0, n):
                result[i] = prefix[i] * suffix[i]

            return result