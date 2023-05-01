# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def all_tree_paths(root):
  if root is None:
    return []
  
  if not root.left and not root.right:
    return [[root.val]]
  
  paths = []
  
  left_sub_paths = all_tree_paths(root.left)
  for sub in left_sub_paths:
    paths.append([root.val, *sub])
    
  right_sub_paths = all_tree_paths(root.right)
  for sub in right_sub_paths:
    paths.append([root.val, *sub])
    
  return paths
  