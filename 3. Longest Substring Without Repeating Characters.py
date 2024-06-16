#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left, ml = 0, 0
        for right, char in enumerate(s):
            if char in chars and chars[char] >= left:
                left = chars[char] + 1
            chars[char] = right
            ml=max(ml, right-left+1)
        return(ml)