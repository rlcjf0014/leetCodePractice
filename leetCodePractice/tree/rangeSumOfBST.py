# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0

        stack = [root]
        result = 0
        while stack:
            curr = stack.pop()
            if curr.left:
                if curr.val >= low:
                    stack.append(curr.left)
            if curr.right:
                if curr.val <= high:
                    stack.append(curr.right)

            if curr.val >= low and curr.val <= high:
                result += curr.val

        return result