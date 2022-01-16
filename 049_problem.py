from prime import prime
from itertools import combinations
list_of_primes = []
for i in range(1000, 10001):
  if prime(i):
    list_of_primes.append(i)
for x in combinations(list_of_primes, 3):
  if "".join(sorted(str(x[0]))) == "".join(sorted(str(x[1]))):
    if "".join(sorted(str(x[1]))) == "".join(sorted(str(x[2]))):
      if x[2] - x[1] == x[1] - x[0]:
        print(x)