def compress(s):
  result = ""
  i = 0
  j = 0
  while j < len(s):
    while j < len(s) and s[j] == s[i]:
      j+=1
    count = "" if j - i == 1 else j-i
    result = result + str(count) + s[i]
    i = j
  return result

# print(compress('ssssbbz'))