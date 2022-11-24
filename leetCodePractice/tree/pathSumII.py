# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []

        stack = [[root, [root.val], root.val]]
        result = []
        while stack:
            curr = stack.pop()
            currNode = curr[0]
            currResult = curr[1]
            currVal = curr[2]
            if not currNode.left and not currNode.right and currVal == targetSum:
                result.append(currResult)
            if currNode.right:
                stack.append([currNode.right, currResult+[currNode.right.val], currVal+currNode.right.val])
            if currNode.left:
                stack.append([currNode.left, currResult+[currNode.left.val], currVal+currNode.left.val])

        return result