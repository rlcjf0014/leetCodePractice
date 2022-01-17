class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        charList=s.split(" ")
        result=[]
        for element in charList:
            newElement=""
            for char in reversed(element):
                newElement+=char
            result.append(newElement)
            
        # return charList
        return ' '.join(result)
        