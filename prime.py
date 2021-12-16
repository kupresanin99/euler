from math import sqrt
import time

def prime(num):
  start_time = time.time()
  starter = 2
  while starter <= sqrt(num):
    if num % starter == 0:
      end_time = time.time()
      print(f"{num} is not prime, took {end_time - start_time:.3f} seconds")
      return False
    starter += 1
    end_time = time.time()
  print(f"{num} is prime, took {end_time - start_time:.3f} seconds")
  return True

# 15 digit prime ~ 12 seconds
# 16 digit prime ~ 12 seconds
# 17 digit prime ~ 49 seconds
# 18 digit prime ~ 158 seconds
# 19 digit prime ~ 411 seconds