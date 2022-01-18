class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # wordArr = s.strip().split(" ")
        # result = [element.strip() for element in wordArr if len(element) != 0]
        # result.reverse()
        # return " ".join(result)
        return " ".join(reversed(s.split()))
       
        
        