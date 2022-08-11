class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                if len(index) == 0:
                    index.append(True)
                    index.append(i)
                else:
                    if index[1] > i:
                        index[1] = i
        
        return index[1] if len(index) > 0 else -1
            