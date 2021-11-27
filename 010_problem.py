def prime(n):
	for i in range(2,round(n/2+2)):
		if(n%i)==0:
			return 0
	return 1

the_sum = 2 + 3 + 5 + 7
for i in range(11, 2000000):
	if prime(i):
		the_sum += i

print(the_sum)