class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        num5 = 0
        num10 = 0
        for num in bills:
            if num == 5:
                num5 += 1
            else:
                if num == 10:
                    num5 -= 1
                    if num5 < 0:
                        return False
                    num10 += 1
                else:
                    if num10 == 0:
                        if num5 < 3:
                            return False
                        else:
                            num5 -= 3
                            if num5 < 0:
                                return False
                    else:
                        num10 -= 1
                        num5 -= 1    
                        if num5 < 0 or num10 < 0:
                            return False

                
        return True