# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

def sum_list(head):
  sum = 0
  while head:
    sum += head.val
    head = head.next
  return sum
