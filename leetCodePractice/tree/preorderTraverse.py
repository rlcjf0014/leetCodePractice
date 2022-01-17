"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack = [root]
        output = []
                   
        while stack:
            root = stack.pop()
            print(root.children, root.val)
            output.append(root.val)
            stack.extend(root.children[::-1])
            
                
        return output 