class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 == 1:
            return False
        stack = []
        for st in s:
            if st == "(" or st == "[" or st == "{":
                stack.append(st)
            else:
                if len(stack) == 0:
                    return False
                curr = stack.pop()
                if st == ")" and curr != "(":
                    return False
                if st == "]" and curr != "[":
                    return False
                if st == "}" and curr != "{":
                    return False
        return True if len(stack) == 0 else False