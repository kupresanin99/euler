from prime import prime

def gcd(x, y):
  if (x == 0):
    return y
  else:
    return gcd(y % x, x)

def totient(entry):
  return sum([1 for x in range(1, entry) if gcd(x, entry) == 1])


my_max_x = 0
my_max_totient = 0
for x in range(2, 1000001):
  if x % 1000 == 0:
    print(x)
  if not prime(x):
    if x % 2 == 0:
      if x % 3 == 0:
        if x % 5 == 0:
          if x % 7 == 0:
            if x % 11 == 0:
              if x % 13 == 0:
                if x % 17 == 0:
                  if x / totient(x) > my_max_totient:
                    my_max_x = x
                    my_max_totient = x / totient(x)
                    print(f"New x: {my_max_x:,.0f} and new totient quotient: {my_max_totient:,.10f}")