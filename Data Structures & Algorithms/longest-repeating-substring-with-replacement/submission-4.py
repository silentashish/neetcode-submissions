from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_length = 0

        for left in range(n):
            freq = defaultdict(int)
            max_freq = 0

            for right in range(left, n):
                freq[s[right]] += 1
                max_freq = max(max_freq, freq[s[right]])

                window_size = right - left + 1

                if window_size - max_freq <= k:
                    max_length = max(max_length, window_size)
                else:
                    break

        return max_length