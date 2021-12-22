from mpmath import *
mp.dps = 150
nums = [mpf(x) ** mpf('0.5') for x in range(1, 100) if x not in [1, 4, 9, 16, 25, 36, 49, 64, 81]]
y = [nstr((x), 102).replace('.', '') for x in nums]
my_sum = 0
for num in y:
  my_sum += sum([int(char) for char in num[:100]])
print(my_sum)