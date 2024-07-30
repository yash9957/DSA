#You are given a string s consisting only of characters 'a' and 'b'​​​​.
#You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.
#Return the minimum number of deletions needed to make s balanced.

class Solution:
    def minimumDeletions(self, s: str) -> int:
        total_a = s.count('a')
        total_b = s.count('b')
        
        # Minimum deletions initialized to the case where we delete all 'a's or all 'b's
        min_deletions = min(total_a, total_b)
        
        # Running count of a's and b's seen so far
        count_a = 0
        count_b = 0
        
        for char in s:
            if char == 'b':
                count_b += 1
            else:
                count_a += 1
            
            # Deletions needed to balance up to this point
            # All 'b's before this point (count_b) and all 'a's after this point (total_a - count_a)
            current_deletions = count_b + (total_a - count_a)
            min_deletions = min(min_deletions, current_deletions)
        
        return min_deletions