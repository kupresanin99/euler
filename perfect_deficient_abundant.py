def perfect_deficient_abundant(num):
  divisors = [1]
  for divisor in range(2, num // 2 + 1): 
    if num % divisor == 0:
      divisors.append(num // divisor)
  divisors.sort()
  my_sum = sum(divisors)
  if my_sum == num:
    num_type = 0
  elif my_sum < num:
    num_type = 1
  else: 
    num_type = 2
  print(divisors)
  print(my_sum)
  print(num_type)

perfect_deficient_abundant(28)