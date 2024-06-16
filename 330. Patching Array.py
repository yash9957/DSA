#Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements in the array.
#Return the minimum number of patches required.


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        missed, i, patches = 1, 0, 0
        while missed <= n:
            if i < len(nums) and nums[i] <= missed:
                missed+=nums[i]
                i+=1
            else:
                missed+=missed
                patches+=1
        return(patches)