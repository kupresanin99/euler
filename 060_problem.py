from prime import prime
from itertools import permutations
from itertools import combinations
print("getting primes")
list_of_primes = []
for i in range (2, 100000):
  if prime(i):
    list_of_primes.append(i)
print("getting 3 tupes")
list_of_primes_to_999 = [x for x in list_of_primes if x <= 6000 and x != 2 and x != 5]
list_of_primes_to_9999 = [x for x in list_of_primes if x <= 22222 and x != 2 and x != 5]
list_of_primes_to_99999 = [x for x in list_of_primes if x <= 34428 and x != 2 and x != 5]
max_concats = 0
list_of_3_tupes = []
list_of_4_tupes = []
list_of_5_tupes = []
for thing in combinations(list_of_primes_to_999, 3):
  prime_counter = 0
  for pair in permutations(thing, 2):
    if not prime(int(str(pair[0]) + str(pair[1]))):
      break
    else:
      prime_counter += 1
  if prime_counter == 6:
    print(f"""{thing} has {prime_counter} prime concats""")
    single_3_tupe = []
    for num in thing:
      single_3_tupe.append(num)
    list_of_3_tupes.append(single_3_tupe)
#print(list_of_3_tupes)
print("Starting 4 tupes")
for tupe_3 in list_of_3_tupes:
  max_3 = max(tupe_3)
  for my_prime in [x for x in list_of_primes_to_9999 if x > max_3]:
    temp_list = tupe_3 + [my_prime]

    prime_counter = 0
    for pair in permutations(temp_list, 2):
      if not prime(int(str(pair[0]) + str(pair[1]))):
        break
      else:
        prime_counter += 1
    if prime_counter == 12:
      print(f"""{temp_list} has {prime_counter} prime concats""")
      single_4_tupe = []
      for num in temp_list:
        single_4_tupe.append(num)
      list_of_4_tupes.append(single_4_tupe)  

print("Starting 5 tupes")
for tupe_4 in list_of_4_tupes:
  max_4 = max(tupe_4)
  for my_prime in [x for x in list_of_primes_to_99999 if x > max_4]:
    temp_list = tupe_4 + [my_prime]

    prime_counter = 0
    for pair in permutations(temp_list, 2):
      if not prime(int(str(pair[0]) + str(pair[1]))):
        break
      else:
        prime_counter += 1
    if prime_counter == 20:
      print(f"""{temp_list} has {prime_counter} prime concats""")
      single_5_tupe = []
      for num in temp_list:
        single_5_tupe.append(num)
      list_of_5_tupes.append(single_5_tupe)

for tupe_5 in list_of_5_tupes:
  print(tupe_5, sum(tupe_5))