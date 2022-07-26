class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        val = None
        for i in range(len(nums)):
            if nums[i] == target:
                if val is None:
                    val = abs(i - start)
                else:
                    val = abs(i-start) if abs(i-start) < val else val
                
        return val