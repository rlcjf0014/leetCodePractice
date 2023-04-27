class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def add_lists(head_1, head_2):
  dummy_head = Node(None)
  tail = dummy_head
  
  carry = 0
  current_1 = head_1
  current_2 = head_2
  while current_1 is not None or current_2 is not None or carry == 1:
    val_1 = 0 if current_1 is None else current_1.val
    val_2 = 0 if current_2 is None else current_2.val
    sum = val_1 + val_2 + carry
    carry = 1 if sum > 9 else 0
    digit = sum % 10
    
    tail.next = Node(digit)
    tail = tail.next
    
    if current_1 is not None:
      current_1 = current_1.next
      
    if current_2 is not None:
      current_2 = current_2.next
      
  return dummy_head.next


#   dummy_head = Node(None)
#   tail = dummy_head
#   curr_1 = head_1
#   curr_2 = head_2
  
#   over_ten = False
#   while curr_1 or curr_2:
#     sum = 0
#     if over_ten == True:
#       sum += 1
#       over_ten = False
#     if curr_1:
#       sum += curr_1.val
#       curr_1 = curr_1.next
#     if curr_2:
#       sum += curr_2.val
#       curr_2 = curr_2.next
#     if sum >= 10:
#       over_ten = True
#       sum = sum % 10
#     new_node = Node(sum)
#     tail.next = new_node
#     tail = new_node
  
#   if over_ten:
#     tail.next = Node(1)
  
#   return dummy_head.next
    

  
  
  
