class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        for i in range(len(s)):
            if (s[i].isalpha() or s[i].isnumeric()):
                string+=s[i].lower()
        return string == string[::-1]