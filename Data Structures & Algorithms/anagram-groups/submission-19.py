class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in range(0, len(strs)):
            item = strs[i]
            sorted_item = ''.join(sorted(item))

            if sorted_item in result:
                continue

            result[sorted_item] = [item]
            for j in range(i+1, len(strs)):
                item_2 = strs[j]
                sorted_item2 = ''.join(sorted(item_2))

                if sorted_item == sorted_item2:
                    result[sorted_item].append(item_2)
                    
        print(result.values())
        return list(result.values())
    




        