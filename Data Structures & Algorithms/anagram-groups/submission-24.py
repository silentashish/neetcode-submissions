from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = defaultdict(list)

        for item in strs:
            sorted_item = ''.join(sorted(item))
            group[sorted_item].append(item)

        return list(group.values())
