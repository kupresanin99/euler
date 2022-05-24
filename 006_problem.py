sum_of_squares = 0
sum_squared = 0

for i in range(101):
	sum_of_squares += i * i
	sum_squared += i

print("The difference is", sum_squared * sum_squared - sum_of_squares)


