#You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
#For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
#Return the head of the modified linked list.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)  # Dummy node to handle edge cases easily
        current = dummy
        sum_value = 0
        node = head.next  # Start from the first node after the initial 0

        while node is not None:
            if node.val == 0:
                # When we encounter a zero, create a new node with the summed value
                if sum_value > 0:
                    current.next = ListNode(sum_value)
                    current = current.next
                    sum_value = 0  # Reset sum for the next segment
            else:
                # Sum the values between zeros
                sum_value += node.val
            
            node = node.next
        return dummy.next