from collections import Counter
list_of_digits = []
for i in range(100, 9999):
  j = "".join(sorted(str(i ** 3)))
  list_of_digits.append(j)
key_permutation = Counter(list_of_digits).most_common(1)[0][0]

for i in range(100, 9999):
  if key_permutation == "".join(sorted(str(i ** 3))):
    print(f"{i} cubed is {i ** 3:,.0f}")
