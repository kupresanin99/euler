from prime import prime
from itertools import permutations
from itertools import combinations

list_of_primes = []
for i in range (2, 100000):
  if prime(i):
    list_of_primes.append(i)

list_of_primes_to_99 = [x for x in list_of_primes if x <= 9999 and x != 2 and x != 5]
max_concats = 0
for thing in combinations(list_of_primes_to_99, 5):
  prime_counter = 0
  for pair in permutations(thing, 2):
    if not prime(int(str(pair[0]) + str(pair[1]))):
      break
    else:
      prime_counter += 1
    print(f"""{thing} has {prime_counter} prime concats""")
  if max_concats == 5:
    break