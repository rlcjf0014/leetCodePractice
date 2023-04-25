# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def is_univalue_list(head):
  check = head.val
  head = head.next
  
  while head:
    if head.val != check:
      return False
    head = head.next
  
  return True
