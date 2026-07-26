class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1 # Fix 1: Set correct initial right bound

        while left <= right:  # Use <= to check the final remaining element
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid      
            
            # Check if the left half is strictly sorted
            if nums[left] <= nums[mid]:
                # Fix 2: Check BOTH bounds to see if target is in this left half
                if nums[left] <= target < nums[mid]:
                    right = mid - 1  # Target is in the left half
                else:
                    left = mid + 1   # Target must be in the right half
            
            # Otherwise, the right half MUST be strictly sorted
            else:
                # Check BOTH bounds to see if target is in this right half
                if nums[mid] < target <= nums[right]:
                    left = mid + 1   # Target is in the right half
                else:
                    right = mid - 1  # Target must be in the left half
            
        return -1