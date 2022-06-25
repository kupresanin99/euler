for a in range(1, 333):
	for b in range (a + 1, 500):
		for c in range(1000 - a - b, 0, -1):
			if c > b:
				if a + b + c == 1000:
					if a * a + b * b == c * c:
						print(a * b * c)
						

