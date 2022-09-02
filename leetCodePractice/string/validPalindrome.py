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