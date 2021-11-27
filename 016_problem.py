import math
num = pow(2, 1000)
tot = 0
for nums in list(str(num)):
	tot += int(nums)
print(tot)