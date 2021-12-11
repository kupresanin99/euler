# For a in [2, 100] and b in [2, 100]
# obtain the distinct set of all
# a^b and b^a  

my_set = {4} # We know 4 is in the result set

for a in range(2, 101):
  temp_list = []
  for b in range(2, 101):
    temp_list.append(a ** b)
    temp_list.append(b ** a)
  my_set = my_set.union(set(temp_list))
  print(f"a = {a} and result set has {len(my_set)} entries")


