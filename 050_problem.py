from prime import prime

list_of_primes = []

for num in range(2, 1000000):
  if prime(num):
    list_of_primes.append(num)

for j in range(2, 555):
  list_length = len(list_of_primes)
  for my_index in range(list_length - j):
    temp_sum = sum(list_of_primes[my_index:my_index + j])
    if temp_sum < 1000000 and temp_sum in list_of_primes:
        print(f"{j} consecutive primes add to prime {temp_sum}")
        break