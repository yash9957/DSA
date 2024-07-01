#Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in arr:
            if i % 2 != 0:
                count += 1
                if count == 3:
                    return(True)
            else:
                count = 0
        return(False)