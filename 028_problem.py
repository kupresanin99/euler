size = 1
my_sum = 1
lap = 1
summand = 1
while size < 1001:
  size += 2
  print(f"size = {size}")
  for i in range(4):
    summand += lap * 2
    my_sum += summand
    print(summand)
  lap += 1
  print(f"Current sum at {my_sum}\n")