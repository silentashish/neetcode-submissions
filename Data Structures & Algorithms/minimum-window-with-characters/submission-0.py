from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        target = Counter(t)
        window = {}

        have = 0
        need = len(target)

        left = 0
        result = [-1, -1]
        min_length = float("inf")

        for right in range(len(s)):
            char = s[right]
            window[char] = window.get(char, 0) + 1

            if char in target and window[char] == target[char]:
                have += 1

            while have == need:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    result = [left, right]

                window[s[left]] -= 1

                if s[left] in target and window[s[left]] < target[s[left]]:
                    have -= 1

                left += 1

        l, r = result
        return "" if min_length == float("inf") else s[l:r+1]