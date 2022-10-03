class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lenSubString = 0
        record = []
        l = 0
        for i in range(len(s)):
            while s[i] in record:
                record.remove(s[l])
                l+=1
            record.append(s[i])
            lenSubString = max(lenSubString, i - l + 1)
        return lenSubString