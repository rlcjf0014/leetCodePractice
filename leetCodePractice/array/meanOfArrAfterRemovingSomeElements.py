class Solution(object):
    def trimMean(self, arr):
        """
        :type arr: List[int]
        :rtype: float
        """
        arr.sort()
        fiveP = int(len(arr) * 0.05)
        newArr = arr[fiveP:len(arr) - fiveP]
        
        return float(sum(newArr)) / float(len(newArr))