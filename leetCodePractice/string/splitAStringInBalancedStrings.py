class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        countR = 0
        countL = 0
        for let in s:
            if let == "R":
                countR += 1
            else:
                countL += 1

            if countR == countL:
                result += 1
                countR = 0
                countL = 0

        return result