# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

# BFS and Queue
def bottom_right_value(root):
  queue = [root]
  
  while queue:
    curr = queue.pop(0)
    if curr.left:
      queue.append(curr.left)
    if curr.right:
      queue.append(curr.right)
  
  return curr.val
  
  