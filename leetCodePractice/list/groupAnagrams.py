class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs) == 1:
            return [[strs[0]]]
        
        record = {}
        result = []
        for element in strs:
            newS = ''.join(sorted(element))
            if newS in record:
                result[record[newS]].append(element)
            else:
                result.append([element])
                record[newS] = len(result) - 1
        return result
                
                
        

        
        