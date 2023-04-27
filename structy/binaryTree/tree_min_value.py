# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
  min_val = float('inf')
  tree_stack = [root]
  
  while tree_stack:
    curr = tree_stack.pop()
    min_val = min(curr.val, min_val)
    if curr.left:
      tree_stack.append(curr.left)
    if curr.right:
      tree_stack.append(curr.right)
  
  return min_val
  
