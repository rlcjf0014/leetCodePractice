class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s) < 2:
            return True

        record = {}
        for letter in s:
            if letter in record:
                record[letter] += 1
            else:
                record[letter] = 1
        
        isOdd = False
        for val in record.values():
            if val % 2 == 1:
                if isOdd == False:
                    isOdd = True
                else:
                    return False

        return True