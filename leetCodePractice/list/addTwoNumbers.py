# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        newHead = None
        newTail = None
        nextDigit = False
        while l1 or l2:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            sum = l1Val + l2Val
            
            if nextDigit == True:
                sum += 1
                
            if sum >= 10:
                nextDigit = True
                sum = sum % 10
            else:
                nextDigit = False
    
            newNode = ListNode(sum)
            if newHead is None:
                newHead = newNode
                newTail = newNode
            else:
                newTail.next = newNode
                newTail = newNode
            
            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            
        if nextDigit == True:
            lastNode = ListNode(1)
            newTail.next = lastNode
            newTail = lastNode
        
        return newHead
            
            
            
        