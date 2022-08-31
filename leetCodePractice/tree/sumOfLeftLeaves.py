# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result=0
        treeStack=[]    
        treeStack.append([root, "r"])
        
        while len(treeStack) != 0:
            curr=treeStack.pop()
            if curr[0].left:
                treeStack.append([curr[0].left, "L"])
            if curr[0].right:
                treeStack.append([curr[0].right, "R"])
            if not curr[0].left and not curr[0].right:
                if curr[1] == "L":
                    result+=curr[0].val
        return result
        