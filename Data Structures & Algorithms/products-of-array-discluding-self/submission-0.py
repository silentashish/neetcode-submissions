class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            n = len(nums)

            result = []
            for i in range(0, n):
                sum = 1
                for j in range(0, n):
                    if i != j:
                        sum *= nums[j]
                result.append(sum)
            return result