class Solution(object):
    def diStringMatch(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        numI = 0
        numD = len(s)
        
        result = []
        
        for letter in s:
            if letter == "I":
                result.append(numI)
                numI+=1
            else:
                result.append(numD)
                numD-=1
        numToAdd = numD if s[-1] == "D" else numI
        result.append(numToAdd)
        
        return result