# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
  if not root:
    return []
  
  bfs_queue = [root]
  result = []
  
  while bfs_queue:
    curr = bfs_queue.pop(0)
    result.append(curr.val)
    if curr.left:
      bfs_queue.append(curr.left)
    if curr.right:
      bfs_queue.append(curr.right)
  
  return result
