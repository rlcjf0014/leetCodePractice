class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        
        
        result = []
        textArr = text.split(" ")
        for i in range(len(textArr)):
            if textArr[i] == first:
                if i+1 < len(textArr):
                    if textArr[i+1] == second:
                        if i+2 < len(textArr):
                            result.append(textArr[i+2])
        return result
        