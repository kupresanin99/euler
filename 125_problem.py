# from pencil and paper, max n = 7071
my_sum = 0
list_of_ints = list(range(1, 7072))
len_of_ints = len(list_of_ints)
my_list_of_results = []

for i in range(1, 7071):
  my_sum += i * i
  if my_sum < 100000000:
    print(f"i={i:,} and sum of squares = {my_sum:,}")
  else:
    break

print(f"Max window to check is i={i - 1}")

for j in range(2, i):
  print(j)
  for k in range(len_of_ints - j + 1):
    temp_result = sum([x * x for x in list_of_ints[k:k + j]])
    if temp_result < 100000000 and str(temp_result) == str(temp_result)[::-1]:
      my_list_of_results.append(temp_result)

my_set_of_results = set(my_list_of_results)

print(sum(my_set_of_results))

# Do not share 