#Given an array of integers nums, sort the array in ascending order and return it.
#You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left: List[int], right: List[int]) -> List[int]:
            sorted_array = []
            i = j = 0
            
            # Merge the two sorted halves
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    sorted_array.append(left[i])
                    i += 1
                else:
                    sorted_array.append(right[j])
                    j += 1
            
            # Append any remaining elements from both halves
            sorted_array.extend(left[i:])
            sorted_array.extend(right[j:])
            
            return sorted_array

        def merge_sort(arr: List[int]) -> List[int]:
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)

        return merge_sort(nums)