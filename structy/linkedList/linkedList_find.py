# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def linked_list_find(head, target):
  while head:
    if head.val == target:
      return True
    head = head.next
  return False
