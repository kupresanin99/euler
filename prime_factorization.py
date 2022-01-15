from prime import prime

def prime_factorization_max_four(num):
  factors = []
  num_temp = num
  for i in range(2, int(num / 2) + 1):
    if prime(i):
      while num_temp % i == 0:
        factors.append(i)
        num_temp /= i
    if len(set(factors)) == 5:
      break
  return factors, len(set(factors))