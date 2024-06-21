#There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
#On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
#When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
#The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
#Return the maximum number of customers that can be satisfied throughout the day.

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        # Calculate base satisfaction without using the technique
        base_satisfaction = 0
        for i in range(n):
            if grumpy[i] == 0:
                base_satisfaction += customers[i]
        
        # Calculate the initial gain from using the technique in the first 'minutes' interval
        max_gain = 0
        current_gain = 0
        for i in range(minutes):
            if grumpy[i] == 1:
                current_gain += customers[i]
        max_gain = current_gain
        
        # Slide the window over the rest of the array
        for i in range(minutes, n):
            if grumpy[i] == 1:
                current_gain += customers[i]
            if grumpy[i - minutes] == 1:
                current_gain -= customers[i - minutes]
            max_gain = max(max_gain, current_gain)
        # The result is the base satisfaction plus the maximum gain
        return base_satisfaction + max_gain