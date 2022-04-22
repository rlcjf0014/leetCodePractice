class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        record = {}
        for word in s1.split(" "):
            if word in record:
                record[word] += 1
            else:
                record[word] = 1
        for word in s2.split(" "):
            if word in record:
                record[word] += 1
            else:
                record[word] = 1
        result = []
        for word in record:
            if record[word] == 1:
                result.append(word)
        
        return result
        
        