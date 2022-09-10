class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        record = []
        for i in range(len(arr)):
            val = arr[i]
            double = val * 2
            arr.pop(i)
            if double in arr:
                return True
            arr.insert(i, val)
        return False