class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        record = {}
        for num in nums:
            values = []
            target = num - diff
            values.append(target)
            if target in nums:
                values.append(nums.index(target))
            else:
                values.append(-1)
            record[num] = values
        
        result = 0
        
        for i in range(len(nums)):
            curr = record[nums[i]]
            if curr[0] in nums:
                if curr[1] >= 0:
                    check = curr[0]
                    if check in nums:
                        second = record[check]
                        if second[1] >= 0 and second[0] in nums:
                            result += 1
                            
        return result
                    
                
        