# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def level_averages(root):
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
  
  result = []
  for level in levels:
    result.append(sum(level) / len(level))
    
  return result
