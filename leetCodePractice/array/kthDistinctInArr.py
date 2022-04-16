class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        result = []
        for x in arr:
            if arr.count(x) == 1:
                result.append(x)
        return result[k-1] if len(result) >= k else ""
        