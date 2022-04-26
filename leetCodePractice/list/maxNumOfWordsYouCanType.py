class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        textArr = text.split()
        output = 0
        for word in textArr:
            letterCount = 0
            for char in brokenLetters:
                if word.count(char) != 0:
                    letterCount += 1
            if letterCount == 0:
                print(word)
                output+=1
            letterCount = 0
        
        return output
                    
                
        