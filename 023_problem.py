from perfect_deficient_abundant import perfect_deficient_abundant
from itertools import combinations_with_replacement

list_of_abundants = []
my_max = 28124
for i in range(2, my_max):
  temp = perfect_deficient_abundant(i)
  if temp[2] == 2:
    list_of_abundants.append(i)
my_ints = []
for thing in combinations_with_replacement(list_of_abundants, 2):
  my_ints.append(sum(thing))
my_ints = [x for x in my_ints if x < my_max]
my_ints = set(my_ints)
all_the_ints = set(list(range(1, my_max)))
my_ints = all_the_ints.difference(my_ints)
print(sum(my_ints))