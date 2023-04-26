class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def insert_node(head, value, index):
  if index == 0:
    new_head = Node(value)
    new_head.next = head
    return new_head
    
  count = 0
  current = head
  while current is not None:
    if count == index - 1:
      temp = current.next
      current.next = Node(value)
      current.next.next = temp
    
    count += 1
    current = current.next
  return head


#   if index == 0:
#     ins = Node(value)
#     ins.next = head
#     return ins
  
#   count = 1
#   curr = head
  
#   while curr:
#     if count == index:
#       next = curr.next
#       ins = Node(value)
#       curr.next = ins
#       ins.next = next
#       break
      
#     count += 1
#     curr = curr.next
  
#   return head
