class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        prev, nxt = 0, n - 1

        while prev < nxt:
            curr_sum = numbers[prev] + numbers[nxt]

            if curr_sum == target:
                return [prev + 1, nxt + 1]

            elif curr_sum < target:
                prev += 1
            else:
                nxt -= 1

        return []