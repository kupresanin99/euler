my_list_of_repunits = [1]
for n in range (2, 40):
  my_list_of_exponents = list(range(n + 1))
  if n <= 4:
    cap = 1000001
  elif n <= 12:
    cap = 251
  else:
    cap = 10
  for i in range(2, cap):
    my_num = sum([i ** x for x in my_list_of_exponents])
    if my_num < 10 ** 12:
      print(n, i, my_num)
      my_list_of_repunits.append(my_num)

my_set = set(my_list_of_repunits)
print(f"The answer might be {sum(my_set):,}")