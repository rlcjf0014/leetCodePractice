# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_levels(root):
  if not root:
    return []
  
  levels = []
  queue = [(root, 0)]
  while queue:
    curr, level_num = queue.pop(0)
    
    if len(levels) == level_num:
      levels.append([curr.val])
    else:
      levels[level_num].append(curr.val)
    
    if curr.left:
      queue.append((curr.left, level_num + 1))
      
    if curr.right:
      queue.append((curr.right, level_num + 1))
    
  return levels
    
    
  
#   queue = [[root]]
#   result = []
#   while queue:
#     curr = queue.pop(0)
#     tempVal = []
#     next = []
#     for node in curr:
#       if node.left:
#         tempVal.append(node.left.val)
#         next.append(node.left)
#       if node.right:
#         tempVal.append(node.right.val)
#         next.append(node.right)
#     result.append(tempVal)
#     queue.append(next)
  
#   return result
        
  
      
      
  