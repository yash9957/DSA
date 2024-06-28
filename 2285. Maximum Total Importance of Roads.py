#You are given an integer n denoting the number of cities in a country. The cities are numbered from 0 to n - 1.
#You are also given a 2D integer array roads where roads[i] = [ai, bi] denotes that there exists a bidirectional road connecting cities ai and bi.
#You need to assign each city with an integer value from 1 to n, where each value can only be used once. The importance of a road is then defined as the sum of the values of the two cities it connects.
#Return the maximum total importance of all roads possible after assigning the values optimally.


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for a,b in roads:
            degrees[a]+=1
            degrees[b]+=1

        sorted_cities = sorted(range(n), key = lambda x: degrees[x], reverse = True)
        value = n
        city_values = [0] * n
        for city in sorted_cities:
            city_values[city] = value
            value-=1
        
        importance = 0
        for i,j in roads:
            importance += city_values[i] + city_values[j]
        
        return(importance)