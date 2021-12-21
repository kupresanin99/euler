import functools
my_nums = []
my_denoms = []
for num in range(10, 99):
  for denom in range(num + 1, 100):
    #print(f"{num} / {denom} = {num / denom:.5f}")
    num_1 = str(num)[0]
    num_2 = str(num)[1]
    num_3 = str(denom)[0]
    num_4 = str(denom)[1]
    if int(num_2) == 0 or int(num_4) == 0:
      pass
    else:
      if num_1 == num_3:
        if int(num_2) / int(num_4) == num / denom:
          print(f"We got a bingo: {num} / {denom} = {num_2} / {num_4} = {num / denom:.5f}")
          my_nums.append(num)
          my_denoms.append(denom)
      if num_1 == num_4:
        if int(num_2) / int(num_3) == num / denom:
          print(f"We got a bingo: {num} / {denom} = {num_2} / {num_3} = {num / denom:.5f}")
          my_nums.append(num)
          my_denoms.append(denom)
      if num_2 == num_4:
        if int(num_1) / int(num_3) == num / denom:
          print(f"We got a bingo: {num} / {denom} = {num_1} / {num_3} = {num / denom:.5f}")
          my_nums.append(num)
          my_denoms.append(denom)
      if num_2 == num_3:
        if int(num_1) / int(num_4) == num / denom:
          print(f"We got a bingo: {num} / {denom} = {num_1} / {num_4} = {num / denom:.5f}")
          my_nums.append(num)
          my_denoms.append(denom)

final_num = functools.reduce(lambda x, y: x * y, my_nums)
final_denom = functools.reduce(lambda x, y: x * y, my_denoms)
print(f"Final fraction: {final_num} / {final_denom} = {final_num / final_denom:.5f}")