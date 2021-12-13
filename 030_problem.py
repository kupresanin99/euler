list_of_bingos = []
for i in range(2, 355000):
  if sum([int(x) ** 5 for x in list(str(i))]) == i:
    print(i)
    list_of_bingos.append(i)
print()
print(sum(list_of_bingos))