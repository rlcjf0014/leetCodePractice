# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        count=0
        treeStack=[]
        treeStack.append([root, root.val])
        while len(treeStack) != 0:
            curr=treeStack.pop()
            currNode=curr[0]
            maxNum = max(currNode.val, curr[1])
            if currNode.val >= maxNum:
                count+=1
            if currNode.left:
                treeStack.append([currNode.left, maxNum])
            if currNode.right:
                treeStack.append([currNode.right, maxNum])
        return count
        