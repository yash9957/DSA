#Given a string s, return the longest palindromic substring in s.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1
            
        for i in range(len(s)):
            # Check for odd-length palindromes
            left1, right1 = expandAroundCenter(s, i, i)
            # Check for even-length palindromes
            left2, right2 = expandAroundCenter(s, i, i + 1)
            
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        
        return s[start:end + 1]