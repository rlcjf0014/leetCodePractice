# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxDepthHelper(root, 0)
        
    def maxDepthHelper(self, root: Optional[TreeNode], count):
        if root is None:
            return count
        count += 1

        return max(self.maxDepthHelper(root.right, count), self.maxDepthHelper(root.left, count))
        
            