def pair_sum(numbers, target_sum):
  record = {}
  for i in range(len(numbers)):
    diff = target_sum - numbers[i]
    if diff in record:
      return (i, record[diff])
    record[numbers[i]] = i