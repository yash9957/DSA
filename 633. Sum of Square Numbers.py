#Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0, int(sqrt(c))
        while a <= b:
            sq = a**2 + b**2
            if sq == c:
                return(True)
            elif sq < c:
                a+=1
            else:
                b-=1
        return(False)