# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
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
        