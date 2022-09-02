# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next            
            prev = prev.next


        prev.next = l1 if l1 is not None else l2

        return prehead.next


        if list1 is None or list2 is None:
            return list1 or list2
        
        newList = None
        tail = None
        
        curr1 = list1
        curr2 = list2
        
        while curr1 and curr2:
            newN = None
            if curr1.val > curr2.val:
                newN = ListNode(curr2.val)
                curr2 = curr2.next
            else:
                newN = ListNode(curr1.val)
                curr1 = curr1.next
                
            if newList is None:
                newList = newN
                tail = newN
            else:
                tail.next = newN
                tail = newN
        
        rest = curr1 or curr2
        tail.next = rest

        
        return newList
            
            
        