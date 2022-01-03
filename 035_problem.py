from prime import prime
import re

list_of_circular_primes = [2, 3, 5, 7]
list_of_primes_to_check = []

# Get all candidate primes (can't have even digit or 5 within)
for num in range(10, 1000001):
  if re.search('0|2|4|5|6|8', str(num)):
    pass
  elif prime(num):
    list_of_primes_to_check.append(num)

for num in list_of_primes_to_check:
  add_to_list_of_circular_primes = True
  checks_to_perform = len(str(num)) - 1
  for i in range(checks_to_perform):
    num = int(str(num)[1:] + str(num)[0])
    if num not in list_of_primes_to_check:
      add_to_list_of_circular_primes = False
  if add_to_list_of_circular_primes == True:
    list_of_circular_primes.append(num)
list_of_circular_primes.sort()
print(list_of_circular_primes)
print(len(list_of_circular_primes))
