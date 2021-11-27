palindromes = []
for a in range(100, 999):
	for b in range(100, 999):
		joe = a * b
		joe1 = list(str(joe))
		joe2 = list(str(joe))
		joe2.reverse()
		if joe1 == joe2:
			palindromes.append(a*b)

print(max(palindromes))