class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                s1, s2 = s[i + 1: j + 1], s[i: j]
                break
            i , j = i + 1, j - 1

        return s1 == s1[::-1] or s2 == s2[::-1]
        
#         if s == s[::-1]:
#             return True
        
        
#         for i in range(len(s)):
#             newS = s[:i] + s[(i+1):]
#             # print(round(len(newS)/2))
#             firstHalf = newS[:math.ceil(len(newS)/2)]
#             secondHalf = newS[math.floor(len(newS)/2):]
#             # print("firstHalf: ", firstHalf)
#             # print("secondHalf: ", secondHalf)
#             if firstHalf == secondHalf[::-1]:
#                 return True
#         return False
    