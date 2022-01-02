# Solutions have to be 2 digits X 3 digits = 4 digits
# 67 X 89 has 4 digits (not enough for pandigital 1-9)
# 123 X 456 has 5 digits (too many for pandigital 1-9)

from itertools import permutations

nine_digits = '123456789'
list_of_bingos = []

for two_dig in permutations(nine_digits, 2):
  temp_2 = ''
  temp_7 = nine_digits
  for digit in two_dig:
    temp_7 = temp_7.replace(digit, '')
    temp_2 += digit
  for three_dig in permutations(temp_7, 3):
    temp_3 = ''
    for digit in three_dig:
      temp_3 += digit
    temp_4 = str(int(temp_2) * int(temp_3))
    temp_9 = ''.join(sorted(temp_2 + temp_3 + temp_4))
    if temp_9 == nine_digits:
      print(f"{temp_2} X {temp_3} = {temp_4}, and digits = {temp_9}")
      list_of_bingos.append(int(temp_4))

for two_dig in permutations(nine_digits, 1):
  temp_2 = ''
  temp_7 = nine_digits
  for digit in two_dig:
    temp_7 = temp_7.replace(digit, '')
    temp_2 += digit
  for three_dig in permutations(temp_7, 4):
    temp_3 = ''
    for digit in three_dig:
      temp_3 += digit
    temp_4 = str(int(temp_2) * int(temp_3))
    temp_9 = ''.join(sorted(temp_2 + temp_3 + temp_4))
    if temp_9 == nine_digits:
      print(f"{temp_2} X {temp_3} = {temp_4}, and digits = {temp_9}")
      list_of_bingos.append(int(temp_4))
print(f"The sum of products is {sum(set(list_of_bingos))}")

