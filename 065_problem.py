list_of_e = [2]
i = 1
for j in range(1, 34):
  list_of_e.append(1)
  list_of_e.append(2 * i)
  list_of_e.append(1)
  i += 1
list_of_e = list_of_e[::-1]

D = list_of_e[0]
N = 1
list_of_e = list_of_e[1:]

for digit in list_of_e:
  N = D * digit + N
  temp = D
  D = N
  N = temp

my_string = str(D)
my_sum = 0
for dig in my_string:
  my_sum += int(dig)
print(f"Numerator = {D:,}")
print(f"Denominator = {N:,}")
print(f"Sum of numerator digits is: {my_sum}")
