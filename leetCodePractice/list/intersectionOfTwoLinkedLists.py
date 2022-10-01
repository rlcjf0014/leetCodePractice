# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        record = {}
        while headA:
            curr = headA.val
            if curr in record:
                record[curr].append(headA)
            else:
                record[curr] = [headA]
            headA = headA.next
        
        while headB:
            curr = headB.val
            if curr in record:
                headInfo = record[curr]
                for head in headInfo:
                    if head == headB:
                        return headB
            headB = headB.next

        return None