my_sum = 0

for i in range(1, 1000001):
  if str(i) == str(i)[::-1]:
    if format(i, 'b') == format(i, 'b')[::-1]:
      print(f"{i} in binary is {format(i, 'b')} and both are palindromes")
      my_sum += i
print()
print(f"Euler 36 answer:  sum = {my_sum}")
