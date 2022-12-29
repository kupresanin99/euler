# The algorithm is attributed to Neelam Yadav

def DistinctSums(n):
  my_string = ""
  placeholder = 0
  table = [0] * (n + 1)
  table[0] = 1
  for i in range(1, n):
    for j in range(i, n + 1):
      table[j] += table[j - i]
      if j == n:
        new_sums = table[n] - placeholder
        placeholder = table[n]
    my_string = f"""Max summand {i},  New Sums = {new_sums:,}\n""" + my_string
  print()
  print(my_string)
  print(f"""The number {n} has {table[n]:,} distinct sums\n""")
  
DistinctSums(100)