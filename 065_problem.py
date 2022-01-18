list_of_e = [2]
i = 1
for j in range(1, 34):
  list_of_e.append(1)
  list_of_e.append(2 * i)
  list_of_e.append(1)
  i += 1
list_of_e = list_of_e[::-1]
print(list_of_e)
D = list_of_e[0]
N = 1
print(D)
list_of_e = list_of_e[1:]
print(list_of_e)

for digit in list_of_e:
  N = D * digit + N
  temp = D
  D = N
  N = temp

  print(f"Numerator = {N:,}")
  print(f"Denominator = {D:,}")
  print(f"{D/N:,.60f}")

my_string = str(D)
my_sum = 0
for dig in my_string:
  my_sum += int(dig)
print(my_sum)
