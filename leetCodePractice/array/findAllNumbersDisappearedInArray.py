import collections

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        record = collections.Counter()
        minimum = 1
        result = []

        for num in nums:
            record[num] += 1
        
        while minimum <= len(nums):
            if minimum not in record:
                result.append(minimum)
            minimum += 1
        
        return result
            
            
            
