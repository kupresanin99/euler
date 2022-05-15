from math import factorial
for i in range(10, 9999999):
	summer = 0
	for letter in str(i):
		summer += factorial(int(letter))
	if summer == i:
		print("Number =", i)
		print("\n\nSuccess!!\n\n")


    