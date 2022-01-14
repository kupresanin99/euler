from math import sqrt

from itertools import combinations

def is_pent(num):
  if ((1 + sqrt(1 + 24 * num)) / 6.0).is_integer():
    return True
  else:
    return False

def is_hex(num):
  if ((1 + sqrt(1 + 8 * num)) / 4.0).is_integer():
    return True
  else:
    return False

for i in range(286, 1000000):
  tri = int((i * (i + 1) / 2))
  if is_pent(tri):
    if is_hex(tri):
      print(f"The {i}th triangle number {tri} is also pent and hex")
      break
  else:
    print(f"{tri} is no good.")