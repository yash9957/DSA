#You are given a binary array nums and an integer k.
#A k-bit flip is choosing a subarray of length k from nums and simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.
#Return the minimum number of k-bit flips required so that there is no 0 in the array. If it is not possible, return -1.
#A subarray is a contiguous part of an array.

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_diff = [0] * (n + 1)  # Difference array to track the flips
        current_flips = 0  # To track the number of ongoing flips affecting the current position
        min_flips = 0

        for i in range(n):
            current_flips ^= flip_diff[i]
            
            # Determine if the current bit is effectively flipped or not
            if nums[i] == (current_flips % 2):
                # If we are at a '0' (which needs to be flipped to '1') but we are out of range for further flips
                if i + k > n:
                    return -1
                # Perform the flip
                current_flips ^= 1
                flip_diff[i] ^= 1
                flip_diff[i + k] ^= 1
                min_flips += 1

        return min_flips