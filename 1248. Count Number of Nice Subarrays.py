#Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
#Return the number of nice sub-arrays.

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_count = {0: 1}
        count_odd = 0
        result = 0
        
        for num in nums:
            if num % 2 == 1:
                count_odd += 1
            
            if count_odd - k in prefix_count:
                result += prefix_count[count_odd - k]
            
            if count_odd in prefix_count:
                prefix_count[count_odd] += 1
            else:
                prefix_count[count_odd] = 1
        return result