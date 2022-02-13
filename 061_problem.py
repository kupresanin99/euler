list_of_tri = []
n = 1
result = 1
while result < 10000:
  result = n * (n + 1) / 2
  if result >= 1000 and result <= 9999:
    list_of_tri.append(int(result))
  n += 1

list_of_square = []
n = 1
result = 1
while result < 10000:
  result = n * n
  if result >= 1000 and result <= 9999:
    list_of_square.append(int(result))
  n += 1

list_of_pent = []
n = 1
result = 1
while result < 10000:
  result = n * (3 * n - 1) / 2
  if result >= 1000 and result <= 9999:
    list_of_pent.append(int(result))
  n += 1

list_of_hex = []
n = 1
result = 1
while result < 10000:
  result = n * (2 * n - 1)
  if result >= 1000 and result <= 9999:
    list_of_hex.append(int(result))
  n += 1

list_of_hept = []
n = 1
result = 1
while result < 10000:
  result = n * (5 * n - 3) / 2
  if result >= 1000 and result <= 9999:
    list_of_hept.append(int(result))
  n += 1

list_of_oct = []
n = 1
result = 1
while result < 10000:
  result = n * (3 * n - 2)
  if result >= 1000 and result <= 9999:
    list_of_oct.append(int(result))
  n += 1

print()
print(list_of_tri)
print()
print(list_of_square)
print()
print(list_of_pent)
print()
print(list_of_hex)
print()
print(list_of_hept)
print()
print(list_of_oct)