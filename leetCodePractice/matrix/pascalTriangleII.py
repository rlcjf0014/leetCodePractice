class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[]
    
        res.append([1])
        
        for i in range(1, rowIndex+1):
            temp = []
            temp.append(1)
            for j in range(1, i):
                temp.append(res[i-1][j-1]+res[i-1][j])
            temp.append(1)
            res.append(temp)
    
        return res[-1]