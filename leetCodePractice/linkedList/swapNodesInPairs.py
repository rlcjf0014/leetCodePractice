# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        first = head
        isFirst = True
        prev = None

        while head and head.next:
            second = head.next
            afterSecond = head.next.next

            if isFirst:
                first = second
                isFirst = False
            
            if prev:
                prev.next = second
            
            prev = head
            second.next = head
            head.next = afterSecond
            head = afterSecond

        return first