# Get a list of descending 9-digit pandigital numbers
# Then check the list for the biggest prime.  
# If none, go on to 8-digit pandigitals, and so on.

from itertools import permutations
from math import sqrt

max_prime = 0

def prime(num):
  starter = 2
  while starter <= sqrt(num):
    if num % starter == 0:
      return False
    starter += 1
  return True

my_digits = '987654321'
my_perms = list(permutations(my_digits))
my_perms = sorted([''.join(x) for x in my_perms], reverse=True)  # Sorted biggest to smallest

for number in my_perms:
  outcome = prime(int(number))
  if outcome == True:
    if int(number) > max_prime:
      max_prime = int(number)

my_digits = '87654321'
my_perms = list(permutations(my_digits))
my_perms = sorted([''.join(x) for x in my_perms], reverse=True)  # Sorted biggest to smallest

for number in my_perms:
  outcome = prime(int(number))
  if outcome == True:
    if int(number) > max_prime:
      max_prime = int(number)

my_digits = '7654321'
my_perms = list(permutations(my_digits))
my_perms = sorted([''.join(x) for x in my_perms], reverse=True)  # Sorted biggest to smallest

for number in my_perms:
  outcome = prime(int(number))
  if outcome == True:
    if int(number) > max_prime:
      max_prime = int(number)

print(f"\nThe biggest prime we found was: {max_prime:,.0f}")
