max_sum = 0
for a in range(1, 100):
  for b in range(1, 100):
    num = a ** b
    temp_sum = 0
    my_string = str(num)
    for digit in my_string:
      temp_sum += int(digit)
    if temp_sum > max_sum:
      max_sum = temp_sum
      print(f"a = {a} to the b = {b} is {a ** b:,.0f} with sum = {max_sum:,.0f}")