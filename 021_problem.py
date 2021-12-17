amicables = []
for num in range(1, 10000):
  my_sum = 0
  for i in range(1, num // 2 + 1):
    if num % i == 0:
      my_sum += i
  my_other_sum = 0
  if my_sum <= 10000:
    for j in range(1, my_sum // 2 + 1):
      if my_sum % j == 0:
        my_other_sum += j

  if (num != my_sum) and (num == my_other_sum):
    print(f"num = {num}, and sum = {my_sum}, and my_other_sum = {my_other_sum}")
    amicables.append(num)
    amicables.append(my_sum)

final_list = sorted(list(set(amicables)))
print()
print(final_list)
print(sum(final_list))