#Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
#As a reminder, a binary search tree is a tree that satisfies these constraints:
#The left subtree of a node contains only nodes with keys less than the node's key.
#The right subtree of a node contains only nodes with keys greater than the node's key.
#Both the left and right subtrees must also be binary search trees.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.accumulated_sum = 0
        def reverse_inorder(node):
            if not node:
                return
            # Traverse the right subtree first (greater values)
            reverse_inorder(node.right)

            # Update the node's value
            self.accumulated_sum += node.val
            node.val = self.accumulated_sum
            
            # Traverse the left subtree
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root