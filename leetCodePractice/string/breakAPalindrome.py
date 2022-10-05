class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) < 2:
            return ""
        
        for i in range(int(len(palindrome) / 2)):
            if palindrome[i] != "a":
                new_str = palindrome[:i] + "a" + palindrome[i+1:]
                return new_str

        return palindrome[:-1] + "b"