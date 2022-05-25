class Solution(object):
    def countPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(i-1, -1, -1):
                if nums[i] == nums[j]:
                    if (i * j) % k == 0:
                        result +=1
        
        
        return result