# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newResult = None
        newEnd = None
        
        while head:
            if head.val == 0:
                merged = 0
                temp = head.next
                while temp and temp.val != 0:
                    merged += temp.val
                    temp = temp.next
                
                if temp:
                    newNode = ListNode(merged)
                    if newResult == None:
                        newResult = newNode
                        newEnd = newNode
                    else:
                        newEnd.next = newNode
                        newEnd = newNode

                head = temp

            else:
                head = head.next

        return newResult
