class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        res = {}
        for num in arr:
            numCount = arr.count(num)
            if num not in res:
                res[num] = numCount
        
        values = res.values()
        for val in values:
            if values.count(val) != 1:
                return False
        return True
        
            
        
        
        
        