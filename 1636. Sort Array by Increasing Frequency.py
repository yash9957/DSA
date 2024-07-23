#Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
#Return the sorted array.

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        sorted_nums = sorted(nums, key=lambda x: (freq[x], -x))
        return sorted_nums