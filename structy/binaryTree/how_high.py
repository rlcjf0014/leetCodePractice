# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# DFS Recursive
def how_high(node):
  if not node:
    return -1

  left_height = how_high(node.left)
  right_height = how_high (node.right)
  
  return 1 + max(left_height, right_height)
