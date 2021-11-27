sum = 0

for i in range(1, 1001):
	sum += i ** i

my_list = list(str(sum))
print(my_list[-10:])
