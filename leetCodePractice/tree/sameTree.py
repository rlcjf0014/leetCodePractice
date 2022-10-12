# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        pstack = [p]
        qstack = [q]

        while pstack and qstack:
            currP = pstack.pop()
            currQ = qstack.pop()
            if currP.val != currQ.val:
                return False

            if currP.left and currQ.left is None:
                return False
            if currP.left is None and currQ.left:
                return False
            if currP.right and currQ.right is None:
                return False
            if currP.right is None and currQ.right:
                return False
            
            if currP.left:
                pstack.append(currP.left)
                qstack.append(currQ.left)
            if currP.right:
                pstack.append(currP.right)
                qstack.append(currQ.right)
        
        return True