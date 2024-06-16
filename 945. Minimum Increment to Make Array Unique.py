#You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
#Return the minimum number of moves to make every value in nums unique.
#The test cases are generated so that the answer fits in a 32-bit integer.


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        count = 0 
        for i in range(1,len(nums)):
            if nums[i] <= nums[i-1]:
                inc = nums[i-1] - nums[i] +1
                nums[i]+=inc
                count+=inc
        return(count)