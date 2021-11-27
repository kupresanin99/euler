num_1s = 0
num_89s = 0
for i in range(1, 10000000):

	target = i
	while target not in (1, 89):
		summer = 0
		for letter in str(target):
			summer += int(letter) * int(letter)
		target = summer
	print("\nNumber =", i)
	print("Target =", target)
	if target == 1:
		num_1s += 1
	else:
		num_89s += 1
print("Number of 1s:", num_1s)
print("Number of 89s:", num_89s)
