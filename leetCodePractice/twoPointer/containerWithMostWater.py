class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            containerH = min(height[l], height[r])
            containerW = r - l
            res = max(containerH * containerW, res)
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return res
            
