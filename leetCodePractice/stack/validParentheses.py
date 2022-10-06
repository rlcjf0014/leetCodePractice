class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for letter in s:
            if letter == "(" or letter == "[" or letter == "{":
                stack.append(letter)
            else:
                if len(stack) == 0:
                    return False
                last = stack.pop()
                if last == "(" and letter != ")":
                    return False
                elif last == "[" and letter != "]":
                    return False
                elif last == "{" and letter != "}":
                    return False
        if len(stack) > 0:
            return False

        return True

        
            
