#There are numBottles water bottles that are initially full of water. You can exchange numExchange empty water bottles from the market with one full water bottle.
#The operation of drinking a full water bottle turns it into an empty bottle.
#Given the two integers numBottles and numExchange, return the maximum number of water bottles you can drink.

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottle_drank, empty_bottles = numBottles, numBottles
        while empty_bottles >= numExchange:
            new_bottle = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange + new_bottle
            bottle_drank += new_bottle
        return(bottle_drank)