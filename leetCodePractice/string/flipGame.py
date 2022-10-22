class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        if len(currentState) == 1:
            return []
        
        result = []
        changed = "--"
        for i in range (len(currentState)-1):
            if currentState[i] == "+" and currentState[i+1] == "+":
                temp = currentState[:i] + changed + currentState[i+2:]
                result.append(temp)

        return result