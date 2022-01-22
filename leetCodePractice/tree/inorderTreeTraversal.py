# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.result = []
        self.dfs(root)
        return self.result
        
    def dfs(self, root):
        if root is None: 
            return
        if root.left:
            self.dfs(root.left)
        if not root.val is None:
            self.result.append(root.val)
        if root.right:
            self.dfs(root.right)
        return