def uncompress(s):
    # Given Solution
    # Use two pointers, i and j to keep track of where is number and where is string
    result = ""
    i = 0
    j = 0
    while j < len(s):
        while s[j].isnumeric():
            j+=1
        tempNum = int(s[i:j])
        result += tempNum * s[j]
        i = j
        j+=1

    return result
  
  # Personal Solution
#   result =""
#   tempNum =""
#   i = 0
#   while i < len(s):
#     while s[i].isnumeric():
#       tempNum = tempNum + s[i]
#       i+=1
#     result = result + (int(tempNum) * s[i])
#     tempNum = ""
#     i+=1
    
#   return result
  

