class Solution(object):
    def findSpecialInteger(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        oneArr = set(arr)
        quarter = len(arr) * 0.25
        for num in oneArr:
            if arr.count(num) > quarter:
                return num
        
            