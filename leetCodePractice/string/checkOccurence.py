class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        book = {}

        for i in range(len(s)):
            if s[i] not in book:
                book[s[i]] = s.count(s[i]);
        
        
        first = book[s[0]];        
        for value in book.values():
            if value != first:
                return False
            
        return True
        