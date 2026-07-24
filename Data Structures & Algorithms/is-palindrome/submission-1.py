import math

class Solution:
    def isPalindrome(self, s_original: str) -> bool:
        # clean the input to remove the non alphanumeric  
        # convert everthing into the small letter
        s_lower = s_original.lower()
        s_formatted = ''.join(c for c in s_lower if c.isalnum())
        # check the length
        n = len(s_formatted)
        # run the loop forward
        for i in range(0, n):
            j = n - i
            if s_formatted[i] != s_formatted[j-1]:
                return False
        return True