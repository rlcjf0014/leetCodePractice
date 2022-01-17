class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result=0
        numRecord = {}
        for num in nums:
            if num in numRecord:
                continue
            else: 
                numRecord[num]=nums.count(num)
        for num in numRecord.values():
            result+=num*(num-1)/2
            
        return result
        
            