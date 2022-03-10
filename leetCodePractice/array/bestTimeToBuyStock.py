class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min = prices[0]
        max = 0
        
        for i in range (len(prices)):
            if prices[i] - min > max:
                max = prices[i] - min
                
            if min > prices[i]:
                min = prices[i]
                
        return max