class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def merge_lists(head_1, head_2):
  fake_head = Node(None)
  tail = fake_head
  curr_1 = head_1
  curr_2 = head_2

  while curr_1 and curr_2:
    if curr_1.val < curr_2.val:
      tail.next = curr_1
      curr_1 = curr_1.next
    else:
      tail.next = curr_2
      curr_2 = curr_2.next
    tail = tail.next


  if curr_1:
    tail.next = curr_1
  if curr_2:
    tail.next = curr_2
  
  
  return fake_head.next
#   new_list = None
#   tail = None
#   curr_1 = head_1
#   curr_2 = head_2
  
#   while curr_1 and curr_2:
#     if curr_1.val < curr_2.val:
#       smaller = curr_1
#       smaller_val = "1"
#       next = curr_1.next
#     else:
#       smaller = curr_2
#       smaller_val = "2"
#       next = curr_2.next
    
#     smaller.next = None
#     if new_list == None:
#       new_list = smaller
#     if tail != None:  
#       tail.next = smaller
#     tail = smaller
    
#     if smaller_val == "1":
#       curr_1 = next
#     else:
#       curr_2 = next

    # return new_list
    
    
      
