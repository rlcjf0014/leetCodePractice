# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def zipper_lists(head_1, head_2):
  curr_1, curr_2 = head_1, head_2
  next_1, next_2 = None, None
  head, tail = None, None
  
  while curr_1 and curr_2:
    next_1, next_2 = curr_1.next, curr_2.next
    curr_1.next, curr_2.next = None, None
    
    if head is None:
      head = curr_1
      tail = curr_1
    else:
      tail.next = curr_1
      tail = curr_1
    
    tail.next = curr_2
    tail = curr_2
    
    curr_1 = next_1
    curr_2 = next_2
    
  if curr_1:
    tail.next = curr_1
  if curr_2:
    tail.next = curr_2
    
  return head
    
    
      
    
    
    
    
  
