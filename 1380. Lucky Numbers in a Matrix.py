#Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
#A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_min = {min(row) for row in matrix}
        col_max = {max(col) for col in zip(*matrix)}
        lucky_numbers = row_min & col_max
        return list(lucky_numbers)