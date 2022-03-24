class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        first = nums[0:n]
        second = nums[n:]
        result = []
        i = 0
        while i != n:
            result.append(first[i])
            result.append(second[i])
            i+=1
        return result
            
        