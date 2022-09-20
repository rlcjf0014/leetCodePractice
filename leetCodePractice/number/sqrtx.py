class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        while num*num <=x: #condition to check 
            num += 1
        return num-1 #return the answer