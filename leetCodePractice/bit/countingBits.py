class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, n+1):
            num = bin(i)[2:]
            result.append(num.count("1"))  
        return result
        