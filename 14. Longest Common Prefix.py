#Write a function to find the longest common prefix string amongst an array of strings.
#If there is no common prefix, return an empty string "".


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for strings in strs[1:]:
            i = 0
            while i < len(prefix) and i < len(strings) and prefix[i] == strings[i]:
                i+=1
            prefix=prefix[:i]
        return prefix