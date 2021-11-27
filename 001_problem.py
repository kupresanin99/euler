list_3_5 = []

for i in range(1, 1000):
  if (i % 3 == 0) | (i % 5 == 0):
  	list_3_5.append(i)

print(sum(list_3_5))