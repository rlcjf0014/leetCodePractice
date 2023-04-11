import math

def is_prime(n):
  if n == 1 or n == 0:
    return False
  
  # Only need to check until the squre root of the number. Concept of corresponding pair
  for i in range(2, int(math.sqrt(n))+1):
    if n % i == 0:
      return False

  return True