#In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
#Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
#Given the integer array position and the integer m. Return the required force.

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        # Sort the positions of the baskets
        position.sort()
        
        # Helper function to check if we can place m balls with at least distance 'force'
        def canPlaceBalls(force):
            count = 1  # Place the first ball in the first basket
            last_position = position[0]
            
            for i in range(1, len(position)):
                if position[i] - last_position >= force:
                    count += 1
                    last_position = position[i]
                    if count == m:
                        return True
            return False
        
        # Binary search for the maximum minimum force
        left, right = 1, position[-1] - position[0]
        
        while left < right:
            mid = (left + right + 1) // 2  # Try for the larger half when tie
            if canPlaceBalls(mid):
                left = mid  # It's possible to place balls with at least 'mid' distance, try for a larger distance
            else:
                right = mid - 1  # It's not possible, reduce the distance
        
        return left