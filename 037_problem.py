from prime import prime
import re

list_of_primes_to_check = []
list_of_bingos = []
num_of_bingos = 0

# Get all candidate primes
# Can't contain 0, 4, 6, 8
# Can't contain 2 or 5 unless it starts with 2 or 5
# Can't start or end with 1
# Can't start or end with 9

for num in range(2, 1000001):
  if re.search('0|4|6|8', str(num))\
    or re.search('2|5', str(num)[1:])\
    or re.search('1', str(num)[0])\
    or re.search('1', str(num)[-1])\
    or re.search('9', str(num)[0])\
    or re.search('9', str(num)[-1]):
    pass
  elif prime(num):
    list_of_primes_to_check.append(num)

for my_prime in list_of_primes_to_check[4:]:
  bingo = True
  string_prime_1 = str(my_prime)
  string_prime_2 = string_prime_1
  my_len = len(string_prime_1)
  for turns in range(my_len - 1):
    string_prime_1 = string_prime_1[1:]
    string_prime_2 = string_prime_2[:-1]
    if prime(int(string_prime_1)) and prime(int(string_prime_2)):
      pass
    else:
      bingo = False
      break
  if bingo == True:
    list_of_bingos.append(my_prime)
    num_of_bingos += 1
    print(f"{my_prime} is the number {num_of_bingos} truncable prime")
print(f"The sum of the truncable primes is {sum(list_of_bingos)}")
