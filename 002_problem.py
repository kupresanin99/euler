x1 = 1
x2 = 2
x3 = 0
fib_list = [x2]

while x3 < 4000000:
	x3 = x1 + x2
	if (x3 < 4000000) & (x3 % 2 == 0):
		fib_list.append(x3)
	x1 = x2
	x2 = x3

print(fib_list)
print(sum(fib_list))