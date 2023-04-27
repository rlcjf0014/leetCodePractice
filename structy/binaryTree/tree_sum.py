# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if not root:
    return 0
  
  tree_stack = [root]
  sum = 0
  while tree_stack:
    curr = tree_stack.pop()
    sum += curr.val
    if curr.left:
      tree_stack.append(curr.left)
    if curr.right:
      tree_stack.append(curr.right)
      
  return sum