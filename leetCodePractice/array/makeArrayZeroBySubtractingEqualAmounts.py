class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = {}
        for num in nums:
            if num != 0:
                if num in record:
                    record[num] += 1
                else:
                    record[num] = 1
        return len(record.keys())