class Solution(object):
    def minCostToMoveChips(self, position):
        """
        :type position: List[int]
        :rtype: int
        """
        even = 0
        for i in position:
            if(i%2==0):
                even+=1
        return min(even,len(position)-even);
            