class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = [tokens[0]]
        i = 1
        while i < len(tokens):
            if tokens[i] == "*" or tokens[i] == "/" or tokens[i] == "+" or tokens[i] == "-":
                firstNum = result.pop()
                secondNum = result.pop()
                if tokens[i] == "*":
                    result.append(int(secondNum) * int(firstNum))
                elif tokens[i] == "/":
                    result.append(int(secondNum) / int(firstNum))
                elif tokens[i] == "+":
                    result.append(int(secondNum) + int(firstNum))
                else:
                    result.append(int(secondNum) - int(firstNum))
            else:
                result.append(tokens[i])

            i+=1
        
        return int(result[0])
            
        