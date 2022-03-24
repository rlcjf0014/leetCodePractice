# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        length = 0
        curr = head
        while curr:
            length+=1
            curr = curr.next
        
        middle = math.floor(length / 2)
        result = head
        while middle != 0:
            result = result.next
            middle-=1
        
        return result