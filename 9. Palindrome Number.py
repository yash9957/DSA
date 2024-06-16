#Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        z=str(x)
        y=z[::-1]
        if z == y:
            return True
        else:
            return False