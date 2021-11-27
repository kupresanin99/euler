j = 2520
truth = True
while truth:
	for i in range(2, 22):
		print("j =", j)
		print("i =", i)
		if j % i == 0:
			pass
		elif i == 21:
			print("The number is", j)
			truth = False
		else:
			j += 1
			print("j now =", j)
			break
