class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        i = 1
        a = n - i
        b = n - (n-i)
        while "0" in str(a) or "0" in str(b):
            i+=1
            a = n - i
            b = n - (n-i)
        
        return [a, b]