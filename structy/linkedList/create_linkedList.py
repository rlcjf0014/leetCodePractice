class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

def create_linked_list(values):
  head = None
  tail = None
  for i in range(len(values)):
    temp = Node(values[i])
    if head == None:
      head, tail = temp, temp
    else:
      tail.next = temp
      tail = temp
  
  return head
      