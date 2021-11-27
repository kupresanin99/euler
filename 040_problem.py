answer = 1
i = 0
m = 0
while i < 1000001:
	m += 1
	word = str(m)
	for letter in word:
		i += 1
		if i in [1, 10, 100, 1000, 10000, 100000, 1000000]:
			answer *= int(letter)
			print("answer now =", answer)
