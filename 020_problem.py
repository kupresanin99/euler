import math
num = math.factorial(100)
tot = 0
for nums in list(str(num)):
	tot += int(nums)
print(tot)