class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        first = edges[0]
        second = edges[1]
        
        node1 = first[0]
        node2 = first[1]
        
        if node1 in second:
            return node1
        else:
            return node2