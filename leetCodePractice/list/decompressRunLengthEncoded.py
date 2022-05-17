class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        
        for i in range(0, len(nums), 2):
            freq = nums[i]
            val = nums[i+1]
            
            while freq > 0:
                result.append(val)
                freq-=1
        
        return result
            
            
        
            
            
            
        