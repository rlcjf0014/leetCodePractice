class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in range(len(s)):
            if (s[i].isalpha() or s[i].isnumeric()):
                string+=s[i].lower()
        return string == string[::-1]


        if len(s) == 0:
            return True
        
        letters = ""
        for letter in s:
            if letter.isalnum():
                letters+=letter.lower()
        
        return letters == letters[::-1]

        i = 0
        j = len(s) - 1

        while i < j:
            while i < len(s) and s[i].isalnum() == False:
                i+=1
            while j > -1 and s[j].isalnum() == False:
                j-=1
            if i >= len(s) or j <= -1:
                break
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        
        return True
