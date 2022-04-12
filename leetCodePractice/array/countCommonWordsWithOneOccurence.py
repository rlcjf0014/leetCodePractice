class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        shorterArr = words2 if len(words1) > len(words2) else words1
        longerArr = words1 if len(words1) > len(words2) else words2
    
        result = 0;
        
        for x in shorterArr:
            if shorterArr.count(x) == 1:
                if x in longerArr and longerArr.count(x) == 1:
                    result+=1
                    
        return result