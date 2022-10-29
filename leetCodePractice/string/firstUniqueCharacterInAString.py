class Solution:
    def firstUniqChar(self, s: str) -> int:
        record = {}
        setVal = set()
        for i in range(len(s)):
            if s[i] in setVal:
                if s[i] in record:
                    del record[s[i]]
            else:
                record[s[i]] = i

            setVal.add(s[i])

        final = list(record.values())
        if not final:
            return -1
        return final[0]

        
