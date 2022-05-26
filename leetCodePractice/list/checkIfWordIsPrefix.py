class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        result = -1
        
        newS = sentence.split()
        lengthW = len(searchWord)
        
        for i in range(len(newS)):
            if newS[i][0:lengthW] == searchWord:
                if result == -1:
                    result = i+1
                else:
                    if i+1 < result:
                        result = i+1
        return result
        
                