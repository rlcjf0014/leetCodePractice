class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        def myFunc(e):
            return e[1]

    

        boxTypes.sort(reverse=True, key=myFunc)
        output = 0
        while truckSize > 0 and len(boxTypes):
            if boxTypes[0][0] == 1:
                curr = boxTypes.pop(0)
                output += curr[1]
            else:
                output += boxTypes[0][1]
                boxTypes[0][0] -= 1
            truckSize -= 1
        return output
            
        