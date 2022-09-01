class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i in range(len(nums)):
            destination = target - nums[i]
            if destination in record:
                return [record[destination], i]
            else:
                record[nums[i]] = i

        record = {}
        for i in range(len(nums)):
            if nums[i] in record:
                val = record[nums[i]]
                return [i, val]
            else:
                diff = target - nums[i]
                record[diff] = i
        
        