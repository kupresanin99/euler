palindromes = []
for a in range(100, 999):
	for b in range(100, 999):
		my_product = a * b
		list_1 = list(str(my_product))
		list_2 = list(str(my_product))
		list_2.reverse()
		if list_1 == list_2:
			palindromes.append(a * b)

print(max(palindromes))



