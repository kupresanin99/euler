sum = 0

for i in range(1, 1001):
	sum += i ** i

my_list = list(str(sum))
print(my_list[-10:])

sum = 0
for j in range(1, 1001):
  sum += j ** j % 10 ** 10
my_list = list(str(sum))
print(my_list[-10:])