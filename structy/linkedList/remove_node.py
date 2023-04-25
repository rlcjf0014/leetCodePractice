# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def remove_node(head, target_val):
  if head.val == target_val:
    return head.next

  current = head
  prev = None
  while current is not None:
    if current.val == target_val:
      prev.next = current.next
      break
    prev = current
    current = current.next
  return head
  
  
#   prev = head
#   curr = prev.next
#   if curr:
#     next = curr.next
  
#   if prev.val == target_val:
#     return curr
  
#   while curr:
#     if curr.val == target_val:
#       prev.next = next
#       return head
#     prev = curr
#     curr = next
#     if next:
#       next = next.next
#     else:
#       next = None
    
#   return head
    
    
      
