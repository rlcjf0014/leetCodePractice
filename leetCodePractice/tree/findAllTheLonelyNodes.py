# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        stack = [root]
        while stack:
            curr = stack.pop()
            if curr.right and curr.left:
                stack.append(curr.right)
                stack.append(curr.left)
            elif curr.left:
                stack.append(curr.left)
                result.append(curr.left.val)
            elif curr.right:
                stack.append(curr.right)
                result.append(curr.right.val)

        return result