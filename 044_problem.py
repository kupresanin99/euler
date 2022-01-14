from math import sqrt

from itertools import combinations

def is_pent(num):
  if ((1 + sqrt(1 + 24 * num)) / 6.0).is_integer():
    return True
  else:
    return False

list_of_pents = []
for i in range(1, 10001):
  list_of_pents.append(int(i * (3 * i - 1) / 2))

for couple in combinations(list_of_pents, 2):
  if(is_pent(abs(couple[1] - couple[0]))):
    if is_pent(couple[0] + couple[1]):
      print(f"{couple} has a difference of {couple[1] - couple[0]:,}")