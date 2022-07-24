class Solution(object):
    
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        
        i = 0
        usage = ""
        while len(usage) < 26:
            if key[i] != " ":
                if key[i] not in usage:
                    usage += key[i]
            i+=1
        
        
        result = ""
        for letter in message:
            if letter == " ":
                result += " "
            else:
                result += chr(usage.index(letter) + 97)
        return result
        