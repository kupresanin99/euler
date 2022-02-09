from factorial import factorial
from collections import Counter

list_of_tuples = []
for n in range(1, 1000001):
  print(n)
  temp_list = [n]
  counter = 0
  while Counter(temp_list).most_common()[0][1] < 2:
    counter += 1
    next_ans = sum([factorial(int(x)) for x in list(str(temp_list[-1]))])
    temp_list.append(next_ans)
  if len(temp_list) - 1 == 60:
    list_of_tuples.append(n)
print(list_of_tuples)
print(len(list_of_tuples))
