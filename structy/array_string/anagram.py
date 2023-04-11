def anagrams(s1, s2):
  s1Record = {}
  s2Record = {}
  
  # can make the counter a separate function
  for i in range(len(s1)):
    if s1[i] in s1Record:
      s1Record[s1[i]] += 1
    else:
      s1Record[s1[i]] = 1
      
  for j in range(len(s2)):
    if s2[j] in s2Record:
      s2Record[s2[j]] += 1
    else:
      s2Record[s2[j]] = 1
  
  # Can use double equals to compare two objects
  return s1Record == s2Record
  
#   if len(s1Record) != len(s2Record):
#     return False
  
#   for key in s1Record:
#     if key not in s2Record:
#       return False
#     if s1Record[key] != s2Record[key]:
#       return False
    
#   return True
  