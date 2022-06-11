class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        output = []
        for i in range(len(arr)-1):
            newArr = arr[i+1:]
            output.append(max(newArr))
        output.append(-1)
        return output