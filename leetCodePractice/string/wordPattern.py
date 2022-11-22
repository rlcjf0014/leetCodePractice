class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        r = set()
        record = {}
        strArr = s.split(" ")
        if len(pattern) != len(strArr):
            return False
            
        for i in range(len(pattern)):
            if pattern[i] not in record:
                if strArr[i] not in r:
                    record[pattern[i]] = strArr[i]
                    r.add(strArr[i])
                else:
                    return False
            else:
                if record[pattern[i]] != strArr[i]:
                    return False

        return True