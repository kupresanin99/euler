# Ordered fractions
# Find the reduced proper fraction that is directly to the left of n/d = 3/7 for d <= 1,000,000

# One strategy, probably not mathematically rigorous or clever is to first take each d and get the largest n/d to the left of 3/7
# Keep track of our current max, append it to a list.

cut_point = 3/7
list_of_fraction_tuples = []
the_overall_max = 0
for i in range(100000, 1000000):
  the_current_max = 0
  # Here we just search in the neighborhood just left of 3/7
  for j in range(int(0.4285 * i), int(0.4286 * i)):
    if j / i < cut_point:
      the_current_max = j / i
    else:
      if the_current_max > the_overall_max:
        list_of_fraction_tuples.append((the_current_max, j - 1, i))
        the_overall_max = the_current_max
      break
print(list_of_fraction_tuples[-1:])