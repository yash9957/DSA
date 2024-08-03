'''You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise.'''

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        return sorted(target) == sorted(arr)




class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        def quicksort(array: List[int]) -> List[int]:
            if len(array) <= 1:
                return array
            pivot = array[len(array) // 2]
            left = [x for x in array if x < pivot]
            middle = [x for x in array if x == pivot]
            right = [x for x in array if x > pivot]
            return quicksort(left) + middle + quicksort(right)

        sorted_target = quicksort(target)
        sorted_arr = quicksort(arr)

        if len(sorted_target) != len(sorted_arr):
            return False

        for i in range(len(sorted_target)):
            if sorted_target[i] != sorted_arr[i]:
                return False

        return True