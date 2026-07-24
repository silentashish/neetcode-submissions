class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num-1 not in nums_set:
                count = 1
                while num + count in nums_set:
                    count += 1
                longest = max(longest, count) 

        return longest