# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def get_node_value(head, index):
  listIndex = 0
  while head:
    if listIndex == index:
      return head.val
    listIndex+=1
    head = head.next
  return None
