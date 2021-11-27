import math

def divisors(n):
    i = 1
    count = 0
    while i <= math.sqrt(n):
        if (n % i == 0):
            if (n / i == i):
                count += 1
            else:
                count += 2
        i = i + 1
    return count

def tri(m):
    tot = 0
    for j in range(1, m + 1):
        tot += j
    return tot

triangle = 0
truthy = True
while truthy == True:
    triangle += 1
    temp_tri = tri(triangle)
    temp_div = divisors(temp_tri)
    if temp_div > 500:
        truthy = False
        print(temp_tri)
        print(temp_div)
