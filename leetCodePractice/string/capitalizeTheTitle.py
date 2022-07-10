class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        strArr = title.split(" ")
        result = []
        for word in strArr:
            if len(word) < 3:
                result.append(word.lower())
            else:
                firstLetter = word[0].upper()
                rest = word[1:].lower()
                result.append(firstLetter+rest)
        return " ".join(result)