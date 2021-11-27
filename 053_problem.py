def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * factorial(n - 1)

the_number = 0
for i in range(1, 101):
    for j in range(0, i+1):
        if factorial(i) / (factorial(j) * factorial(i-j)) > 1000000:
            print(i, j, i + 1 - 2 * j)
            the_number += i + 1 - 2 * j
            break
print(the_number)


