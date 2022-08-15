class Solution(object):
    
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        def isOdd(num):
            if num % 2 == 1:
                return True
            return False
        
        for i in range(0, len(arr)):
            if i+2 < len(arr):
                if isOdd(arr[i]) and isOdd(arr[i+1]) and isOdd(arr[i+2]):
                    return True
            
        return False
        