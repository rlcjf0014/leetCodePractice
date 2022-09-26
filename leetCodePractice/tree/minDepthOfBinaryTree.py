# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        result = 0
        stack = [[root]]
        while stack:
            curr = stack.pop(0)
            result += 1
            temp = []
            for i in range(len(curr)):
                if not curr[i].right and not curr[i].left:
                    return result
                if curr[i].right:
                    temp.append(curr[i].right)
                if curr[i].left:
                    temp.append(curr[i].left)
            stack.append(temp)

        return result
            