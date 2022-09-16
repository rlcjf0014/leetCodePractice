class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"

        result = []
        
        for word in words:
            temp = None
            oneRow = True
            for i in range(len(word)):
                curr = word[i].lower()
                row = None
                if curr in row1:
                    row = "row1"
                elif curr in row2:
                    row = "row2"
                else:
                    row = "row3"
                if temp is None:
                    temp = row
                elif temp != row:
                    oneRow = False
                    break
            if oneRow:    
                result.append(word)
                
        return result
                    
            