class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)

        left = 0
        right  = n-1

        max_area = 0

        while left < right and right < n:
            b = abs(left - right)
            h = min(heights[left], heights[right])

            area = b * h
            max_area = max( area, max_area)

            if heights[left] < heights[right]:
                left += 1
            
            else:
                right -= 1
        
        return max_area


