class Solution(object):
    def maxDistance(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        distance=0
        for i in range(0,len(colors)):
            for j in range(len(colors)-1,i-1,-1):
                if colors[i]!= colors[j]:
                    distance=max(distance,j-i)
                    break
        return distance
            