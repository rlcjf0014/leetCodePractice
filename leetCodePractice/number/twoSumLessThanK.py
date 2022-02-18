class Solution(object):
    def twoSumLessThanK(self, nums, k):
        result = -1
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum < k:
                    result = max(result, sum)
        return result
        