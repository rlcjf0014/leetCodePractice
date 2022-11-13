class Solution:
    def reverseWords(self, s: str) -> str:
        strArr = s.strip().split(" ")
        result = list(filter(lambda x: len(x) != 0, strArr))
        return " ".join(result[::-1])
                