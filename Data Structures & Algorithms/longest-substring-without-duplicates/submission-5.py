class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        longest = 0

        for ch in s:
            if ch in lst:
                while ch in lst:
                    lst.pop(0)

            lst.append(ch)
            longest = max(longest, len(lst))

        return longest