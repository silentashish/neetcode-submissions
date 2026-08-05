class Solution:
    def hammingWeight(self, n: int) -> int:
        n_bin = str(bin(n)[2:])

        count = 0
        for item in n_bin:
            if item == '1':
                count += 1
        return count

        