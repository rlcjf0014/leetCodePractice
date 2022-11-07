# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        tenthDigit = False
        first = None
        end = None

        while l1 and l2:
            valSum = l1.val + l2.val
            if tenthDigit:
                valSum += 1

            if valSum > 9:
                tenthDigit = True
                valSum = valSum % 10
            else:
                tenthDigit = False
            
            newNode = ListNode(valSum)
            if first:
                end.next = newNode
                end = newNode
            else:
                first = newNode
                end = newNode

            l1 = l1.next
            l2 = l2.next
        
        temp = l1 or l2

        while temp:
            valSum = temp.val
            if tenthDigit:
                valSum += 1

            if valSum > 9:
                tenthDigit = True
                valSum = valSum % 10
            else:
                tenthDigit = False

            newNode = ListNode(valSum)
            if first:
                end.next = newNode
                end = newNode
            else:
                first = newNode
                end = newNode

            temp = temp.next
        
        if tenthDigit:
            newNode = ListNode(1)
            if first:
                end.next = newNode
                end = newNode
            else:
                first = newNode
                end = newNode

        return first

