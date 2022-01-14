from prime import prime
list_of_primes = []
list_of_odd_composites = []
list_of_mults = []
for i in range(2, 100000):
  if prime(i):
    list_of_primes.append(i)
for j in range(2, 200000):
  if not prime(j) and j % 2 == 1:
    list_of_odd_composites.append(j)
for my_prime in list_of_primes:
  for k in range(1, 1000):
    list_of_mults.append(my_prime + 2 * k * k)
my_diff = set(list_of_odd_composites).difference(set(list_of_mults))
print(my_diff)