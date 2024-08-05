'''A distinct string is a string that is present only once in an array.

Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

Note that the strings are considered in the order in which they appear in the array.'''

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        arr_rep = []
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        distinct_strings = [string for string in arr if freq[string] == 1]
        
        if k <= len(distinct_strings):
            return distinct_strings[k-1]
        else:
            return ""
        

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        arr_rep = []
        for i in arr:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
        for i in freq:
            if freq[i] == 1:
                arr_rep.append(i)

        if len(arr_rep) < k:
            return ("")
        else:
            return (arr_rep[k-1])