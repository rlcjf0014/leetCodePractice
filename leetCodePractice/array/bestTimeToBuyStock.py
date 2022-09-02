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

        

        minimum = prices[0]
        maximum = 0
        
        for i in range(1, len(prices)):
            if prices[i] - minimum > maximum:
                maximum = prices[i] - minimum
            
            if minimum > prices[i]:
                minimum = prices[i]
                
        return maximum