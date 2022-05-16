class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        index = 0
        
        while index < len(arr):
            if arr[index] == 0:
                arr.insert(index, 0)
                arr.pop(-1)
                index+=1
            index+=1
                
            