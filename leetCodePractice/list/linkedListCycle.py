# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        record = set()
        curr = head
        while curr:
            if curr in record:
                return True
            record.add(curr)
                
            curr = curr.next
            
        return False
        