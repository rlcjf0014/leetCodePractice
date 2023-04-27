# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
  if not root:
    return False
  
  tree_stack = [root]
  
  while tree_stack:
    curr = tree_stack.pop()
    if curr.val == target:
      return True
    if curr.left:
      tree_stack.append(curr.left)
    if curr.right:
      tree_stack.append(curr.right)
  
  return False
  