#Given a positive integer num, return true if num is a perfect square or false otherwise.
#A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
#You must not use any built-in library function, such as sqrt.


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l+r)//2
            mids = mid*mid
            if mids < num:
                l = mid+1
            elif mids == num:
                return(True)
            else:
                r = mid -1
        return(False)