# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = [[root.val]]
        stack = [[root]]

        while stack:
            temp = []
            level = []
            curr = stack.pop(0)
            for node in curr:
                if node.left:
                    level.append(node.left)
                    temp.append(node.left.val)
                if node.right:
                    level.append(node.right)
                    temp.append(node.right.val)
            if temp:
                result.append(temp)
            if level:
                stack.append(level)
        
        return result

