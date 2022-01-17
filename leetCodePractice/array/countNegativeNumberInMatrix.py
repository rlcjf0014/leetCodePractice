class Solution(object):
    def countNegatives(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result=0
        for group in grid:
            for num in group:
                if num < 0:
                    result += 1
                    
        return result