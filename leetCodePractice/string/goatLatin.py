class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        result=''
        part=sentence.split()
        for i in range(len(part)):
            if part[i][0] in 'aeiouAEIOU':
                result+=part[i]+'m'+'a'*(i+2)+' '
            else:
                result+=part[i][1:]+part[i][0]+'m'+'a'*(i+2)+' '
        return result[:-1]