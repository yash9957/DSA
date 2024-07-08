#There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        winner = 0
        for i in range(2, n + 1):
            winner = (winner + k) % i
        return winner + 1