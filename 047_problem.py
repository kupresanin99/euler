from threading import main_thread
from prime_factorization import prime_factorization_max_four
list_of_nums = [-100, -50, -25, -10]
min_gap = 90
for i in range(21111, 10000001):
  mt = prime_factorization_max_four(i)
  if mt[1] == 4:
    list_of_nums = list_of_nums[1:]
    list_of_nums.append(i)
    factor_list = list(set(mt[0]))
    factor_list.sort()
    if list_of_nums[3] - list_of_nums[0] < min_gap:
      min_gap = list_of_nums[3] - list_of_nums[0]
    print(f"{i} factors as {factor_list} with gap = {list_of_nums[3] - list_of_nums[0]} and min_gap = {min_gap}")
  if list_of_nums[3] - list_of_nums[0] == 3:
    break  