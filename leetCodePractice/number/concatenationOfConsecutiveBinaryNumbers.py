class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = ""
        i = 0
        while i <= n:
            temp = format(i, "b")  
            result += temp
            i+=1
        
        return int(result, 2) % (10**9 + 7)