from math import sqrt

def prime(num):
  starter = 2
  while starter <= sqrt(num):
    if num % starter == 0:
      return False
    starter += 1
  return True
