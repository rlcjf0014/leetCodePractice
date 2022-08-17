class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        indices = []
        for i in range(len(s)):
            if s[i] == c:
                indices.append(i)
                
        indices.sort()
        result = []
        i = 0
        while len(result) != len(s):
            lowest = abs(indices[0] - i)
            for num in indices:
                diff = abs(num - i)
                if diff < lowest:
                    lowest = diff
                
    
            result.append(lowest)
            i+=1
        return result