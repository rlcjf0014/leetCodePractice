class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        record = {}
        for alpha in text:
            if alpha in record:
                record[alpha] += 1
            else:
                record[alpha] = 1
            
        result = 0
        while ("l" in record and "o" in record) and (record["l"] >= 2 and record["o"] >=2 ):
            record["l"] -= 2
            record["o"] -= 2
            
            if "b" in record and record["b"] > 0:
                if "a" in record and record["a"] > 0:
                    if "n" in record and record["n"] > 0:
                        record["b"] -= 1
                        record["a"] -= 1
                        record["n"] -= 1
                        result += 1
                        
        return result
                
        