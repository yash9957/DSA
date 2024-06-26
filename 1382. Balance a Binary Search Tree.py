#Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.
#A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Helper function to perform in-order traversal and collect nodes
        def inorder_traversal(node):
            if not node:
                return []
            return inorder_traversal(node.left) + [node.val] + inorder_traversal(node.right)
        
        # Helper function to build a balanced BST from sorted array
        def build_balanced_bst(nums):
            if not nums:
                return None
            mid = len(nums) // 2
            root = TreeNode(nums[mid])
            root.left = build_balanced_bst(nums[:mid])
            root.right = build_balanced_bst(nums[mid + 1:])
            return root
        
        # Get sorted node values from the BST
        sorted_vals = inorder_traversal(root)
        
        # Build and return the balanced BST
        return build_balanced_bst(sorted_vals)