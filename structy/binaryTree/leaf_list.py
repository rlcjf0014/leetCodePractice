# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def leaf_list(root):
  if not root:
    return []
  
  result = []
  stack = [root]
  while stack:
    curr = stack.pop()
    if curr.right:
      stack.append(curr.right)
    if curr.left:
      stack.append(curr.left)
    if not curr.right and not curr.left:
      result.append(curr.val)
  
  return result
