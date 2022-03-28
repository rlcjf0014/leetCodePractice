class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        sum = 0
        for i in range(len(items)):
            temp = items[i]
            if ruleKey == "type":
                if temp[0] == ruleValue:
                    sum+=1
            elif ruleKey == "color":
                if temp[1] == ruleValue:
                    sum+=1
            else:
                if temp[2] == ruleValue:
                    sum+=1
        return sum
            