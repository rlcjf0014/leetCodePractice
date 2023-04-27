# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def depth_first_values(root):
  # Iterative Solution
  if not root:
    return []

  stack = [root]
  values = []
  
  while stack:
    node = stack.pop()
    values.append(node.val)
    if node.right:
      stack.append(node.right)
    if node.left:
      stack.append(node.left)
  return values


#   if not root:
#     return []
  
#   dfs_stack = [root]
#   result = []
#   while dfs_stack:
#     curr = dfs_stack.pop()
#     if curr.right:
#       dfs_stack.append(curr.right)
#     if curr.left:
#       dfs_stack.append(curr.left)
#     result.append(curr.val)
#   return result