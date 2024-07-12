#You are given a string s and two integers x and y. You can perform two types of operations any number of times.
#Remove substring "ab" and gain x points.
#For example, when removing "ab" from "cabxbae" it becomes "cxbae".
#Remove substring "ba" and gain y points.
#For example, when removing "ba" from "cabxbae" it becomes "cabxe".
#Return the maximum points you can gain after applying the above operations on s.


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def points_scored(s: str, first_str: str, first_points: int, second_str: str, second_points: int):
            stack = []
            total_points = 0
            for char in s:
                if stack and stack[-1] + char == first_str:
                    stack.pop()
                    total_points+=first_points
                else:
                    stack.append(char)
            
            new_stack = []
            for char in stack:
                if new_stack and new_stack[-1] + char == second_str:
                    new_stack.pop()
                    total_points+=second_points
                else:
                    new_stack.append(char)
            
            return(total_points)

        if x >= y:
            return points_scored(s, "ab", x, "ba", y)
        else:
            return points_scored(s, "ba", y, "ab", x)