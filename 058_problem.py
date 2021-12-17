# Start at i = 1 for each wrap-around
# Layer = i
# Length of side = 2i + 1
# Length of wrap-around = 8i
# Denominator = 4i + 1
# Check primes 1, +2i, +2i, +2i, +2i (4x, then increment i += 1)

from prime import prime
start_num = 1

num_primes = 0
under_10 = False
i = 1
while not under_10:
  side_length = 2 * i + 1
  denom = 4 * i + 1
  for j in range(1, 5):
    start_num += 2 * i
    if prime(start_num):
      print(f"""{start_num} is prime""")
      num_primes += 1
  print(f"Layer {i} complete")
  print(f"Number of primes = {num_primes}")
  print(f"Side length = {side_length}")
  print(f"Denom = {denom}")
  print(f"Prime ratio = {num_primes / denom:,.20f}")
  print()
  if num_primes / denom < 0.10:
    under_10 = True
  i += 1