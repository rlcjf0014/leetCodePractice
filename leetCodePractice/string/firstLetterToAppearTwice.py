class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        record = []
        i = 0
        while result == "":
            if s[i] in record:
                result = s[i]
            else:
                record.append(s[i])
            i+=1
        return result