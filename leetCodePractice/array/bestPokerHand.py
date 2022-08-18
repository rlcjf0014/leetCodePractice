class Solution(object):
    def bestHand(self, ranks, suits):
        """
        :type ranks: List[int]
        :type suits: List[str]
        :rtype: str
        """
        def checkFlush(suits):
            result = True
            initial = suits[0]
            for i in range(1, len(suits)):
                if suits[i] != initial:
                    result = False
                    break
            return result
        
        def checkRest(ranks):
            record = {}
            for num in ranks:
                if num in record:
                    record[num] += 1
                else:
                    record[num] = 1
            numbers = record.values()
            numbers.sort(reverse=True)
            if numbers[0] >= 3:
                return "Three of a Kind"
            elif numbers[0] >= 2:
                return "Pair"
            else:
                return "High Card"
            
            return True if numbers[0] >= 3 else False
    
        
        if checkFlush(suits):
            return "Flush"
        else:
            return checkRest(ranks)
    