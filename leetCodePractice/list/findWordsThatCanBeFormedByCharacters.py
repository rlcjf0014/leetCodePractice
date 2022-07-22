class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        result = []
        sample = chars
        for word in words:
            for letter in word:
                if letter in sample:
                    sample = sample.replace(letter,'', 1)
                else:
                    sample = chars
                    break
            if len(sample) != len(chars):
                result.append(word)
            sample = chars
                
        sum = 0
        for target in result:
            sum += len(target)
        return sum