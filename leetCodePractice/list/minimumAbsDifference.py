class Solution(object):
    def minimumAbsDifference(self, arr):
        """
        :type arr: List[int]
        :rtype: List[List[int]]
        """
        arr.sort()
        result = [[arr[0], arr[1]]]
        absolute = abs(arr[0]-arr[1])
        for i in range(1, len(arr)-1):
            comp = abs(arr[i] - arr[i+1])
            if comp < absolute:
                absolute = comp
                result = [[arr[i], arr[i+1]]]
            elif comp == absolute:
                result.append([arr[i], arr[i+1]])
            else:
                next
        return result
                