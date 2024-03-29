# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        stack = [[root, root.val]]
        while stack:
            curr = stack.pop()
            currNode = curr[0]
            currVal = curr[1]
            if not currNode.left and not currNode.right and currVal == targetSum:
                return True
            if currNode.right:
                stack.append([currNode.right, currVal+currNode.right.val])
            if currNode.left:
                stack.append([currNode.left, currVal+currNode.left.val])
        return False