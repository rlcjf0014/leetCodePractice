# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]: 
        nextN = None
        prev = None

        while head:
            nextN = head.next
            head.next = prev
            prev = head
            head = nextN
            
        return prev
                
