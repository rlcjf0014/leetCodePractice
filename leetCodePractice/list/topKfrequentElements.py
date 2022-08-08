class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        record = {}
        for num in nums:
            if num in record:
                record[num] += 1
            else:
                record[num] = 1
    
        valuesToUse = record.values()
        if len(valuesToUse) == 0:
            return []
        target = []
        
        while k != 0 and len(valuesToUse) != 0:
            maxNum = max(valuesToUse)
            target.append(maxNum)
            valuesToUse.remove(maxNum)
            k-=1
            
        result = []
        
        for x, y in record.items():
            if y in target:
                result.append(x)
                
        return result
        
        
            