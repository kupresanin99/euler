biggest_repetend = 0
biggest_num = 0
for i in range(1, 1000):
  j = i
  check_2 = True
  check_5 = True
  while check_2:
    if i % 2 == 0:
      i //= 2
    else:
      check_2 = False
  while check_5:
    if i % 5 == 0:
      i //= 5
    else:
      check_5 = False
  found_repetend = False
  n = 0
  while not found_repetend:
    n += 1
    if (10 ** n - 1) % i == 0:
      print(f"Number {j} has repetend length of {n}")
      found_repetend = True
    if n > biggest_repetend:
      biggest_repetend = n
      biggest_num = j

print(f"Looks like {biggest_num} has a repetend of {biggest_repetend}")
