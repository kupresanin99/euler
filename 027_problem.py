from prime import prime
max_chain = 0
best_a = 10001
best_b= 10001

# believe n^2 + an + b must have b prime to generate primes since starting at n = 0
bs = []
for num in range(2, 1000):
  if prime(num):
    bs.append(num)

# start with a = +- 999 and work down to a = 0

for a in range(999, -1, -1):
  for b in bs:
    my_chain = 0 
    is_prime = True
    n = 0
    while is_prime == True:
      if prime(n * n + a * n + b):
        my_chain += 1
        n += 1
      else:
        if n > 40:
          print(f"a={a} and b={b} had streak of n={n}")
        is_prime = False
    if my_chain > max_chain:
      max_chain = my_chain
      best_a = a
      best_b = b

    my_chain = 0 
    is_prime = True
    n = 0
    while is_prime == True:
      if n * n - a * n + b >= 2:
        if prime(n * n - a * n + b):
          my_chain += 1
          n += 1
        else:
          if n > 40:
            print(f"a={-a} and b={b} had streak of n={n}")
          is_prime = False
      else:
        is_prime = False
    if my_chain > max_chain:
      max_chain = my_chain
      best_a = -a
      best_b = b

print(f"Best streak is n={max_chain} with a={best_a} and b={best_b}")
