class Solution(object):
    def numberOfMatches(self, n):
        """
        :type n: int
        :rtype: int
        """
        total = 0
        num = 0
        while n is not 1:
            if n % 2 == 0:
                num = n / 2
            else:
                num = (n - 1) / 2
            total += num
            n -= num
                
        return total