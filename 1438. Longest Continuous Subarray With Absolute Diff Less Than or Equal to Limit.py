#Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        min_deque = deque()
        max_deque = deque()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            # Maintain the min_deque
            while min_deque and nums[min_deque[-1]] > nums[right]:
                min_deque.pop()
            min_deque.append(right)
            
            # Maintain the max_deque
            while max_deque and nums[max_deque[-1]] < nums[right]:
                max_deque.pop()
            max_deque.append(right)
            
            # Ensure the window is valid
            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                # Remove elements that are out of the current window
                if min_deque[0] < left:
                    min_deque.popleft()
                if max_deque[0] < left:
                    max_deque.popleft()
            
            # Update the max_len
            max_len = max(max_len, right - left + 1)
        
        return max_len