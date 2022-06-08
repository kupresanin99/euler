counter = 4
number = 10

while counter < 10001:
	number += 1
	if number % 2 == 0:
		pass
	else:
		prime = True
		for i in range(3, number // 2):
			if number % i == 0:
				prime = False
				break
		if prime == True:
			counter += 1
			print("number", number, "is the", counter, "prime number")

