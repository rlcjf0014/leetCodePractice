def intersection(a, b):
  dataA = set(a)
    
  result = []
  for num2 in b:
    # accessing set is O(1)
    if num2 in dataA:
      result.append(num2)
  
  return result
  


# print(intersection([4,2,1,6], [3,6,9,2,10]))