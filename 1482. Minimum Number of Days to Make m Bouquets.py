#You are given an integer array bloomDay, an integer m and an integer k.
#You want to make m bouquets. To make a bouquet, you need to use k adjacent flowers from the garden.
#The garden consists of n flowers, the ith flower will bloom in the bloomDay[i] and then can be used in exactly one bouquet.
#Return the minimum number of days you need to wait to be able to make m bouquets from the garden. If it is impossible to make m bouquets return -1.


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return(-1)
        # Helper function to check if we can make m bouquets in given days
        def canMakeBouquets(days):
            bouquets = 0
            flowers = 0
            
            for bloom in bloomDay:
                if bloom <= days:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0

                if bouquets >= m:
                    return True
            
            return False

        # Binary search to find the minimum days
        low, high = min(bloomDay), max(bloomDay)

        while low < high:
            mid = (low + high) // 2
            if canMakeBouquets(mid):
                high = mid
            else:
                low = mid + 1
        return low