class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0

        for num in nums_set:
            if num-1 not in nums_set:
                count = 1
                seek = num
                while seek + 1 in nums_set:
                    count += 1
                    seek += 1
                longest = max(longest, count) 

        return longest