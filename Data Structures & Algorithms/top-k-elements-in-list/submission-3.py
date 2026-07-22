from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)

        for item in nums:
            count[item] +=  1

        sorted_keys = sorted(count, key = count.get, reverse= True)

        return sorted_keys[:k]