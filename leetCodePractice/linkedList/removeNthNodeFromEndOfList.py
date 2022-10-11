# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenList = 1
        curr = head
        while curr.next:
            curr = curr.next
            lenList += 1
    
        if n == lenList or n > lenList:
            return head.next
        
        prev = head
        temp = head
        i = lenList - n
        while i > 0:
            prev = temp
            temp = temp.next
            i -= 1
        
        prev.next = temp.next
        return head
        



