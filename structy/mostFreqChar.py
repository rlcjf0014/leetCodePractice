def most_frequent_char(s):
  record = {}
  for i in range(len(s)):
    if s[i] in record:
      record[s[i]] += 1
    else:
      record[s[i]] = 1
  mostChar = ""
  count = 0
  for key in record:
    if record[key] > count:
      count = record[key]
      mostChar = key
  
  return mostChar