def five_sort(nums):
  i = 0
  j = len(nums) - 1
  while i <= j:
    if nums[j] == 5:
      j -= 1
    elif nums[i] == 5:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    else:
      i += 1
  return nums

  # initial personal solution
#   i = 0
#   j = len(nums) - 1
#   while i < j:
#     while nums[j] == 5:
#       j -= 1
#     while nums[i] != 5:
#       i += 1
#     if i >=j:
#       break;
#     temp = nums[i]
#     nums[i] = nums[j]
#     nums[j] = temp


    
  return nums