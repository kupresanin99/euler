list_of_tri = []
n = 1
result = 1
while result < 10000:
  result = n * (n + 1) / 2
  if result >= 1000 and result <= 9999 and result % 10 != 0 and (result // 10) % 10 != 0 and (result // 100) % 10 != 0:
    list_of_tri.append(int(result))
  n += 1

list_of_square = []
n = 1
result = 1
while result < 10000:
  result = n * n
  if result >= 1000 and result <= 9999 and result % 10 != 0 and (result // 10) % 10 != 0 and (result // 100) % 10 != 0:
    list_of_square.append(int(result))
  n += 1

list_of_pent = []
n = 1
result = 1
while result < 10000:
  result = n * (3 * n - 1) / 2
  if result >= 1000 and result <= 9999 and result % 10 != 0 and (result // 10) % 10 != 0 and (result // 100) % 10 != 0:
    list_of_pent.append(int(result))
  n += 1

list_of_hex = []
n = 1
result = 1
while result < 10000:
  result = n * (2 * n - 1)
  if result >= 1000 and result <= 9999 and result % 10 != 0 and (result // 10) % 10 != 0 and (result // 100) % 10 != 0:
    list_of_hex.append(int(result))
  n += 1

list_of_hept = []
n = 1
result = 1
while result < 10000:
  result = n * (5 * n - 3) / 2
  if result >= 1000 and result <= 9999 and result % 10 != 0 and (result // 10) % 10 != 0 and (result // 100) % 10 != 0:
    list_of_hept.append(int(result))
  n += 1

list_of_oct = []
n = 1
result = 1
while result < 10000:
  result = n * (3 * n - 2)
  if result >= 1000 and result <= 9999 and result % 10 != 0 and (result // 10) % 10 != 0 and (result // 100) % 10 != 0:
    list_of_oct.append(int(result))
  n += 1

set_of_first_two = set()
for digs_12 in list_of_tri + list_of_square + list_of_pent + list_of_hex + list_of_hept + list_of_oct:
  set_of_first_two.add(str(digs_12)[:2])

set_of_last_two = set()
for digs_34 in list_of_tri + list_of_square + list_of_pent + list_of_hex + list_of_hept + list_of_oct:
  set_of_last_two.add(str(digs_34)[2:])

good_digits = set_of_first_two.intersection(set_of_last_two)

list_of_tri = [x for x in list_of_tri if str(x)[:2] in good_digits and str(x)[2:] in good_digits]
list_of_square = [x for x in list_of_square if str(x)[:2] in good_digits and str(x)[2:] in good_digits]
list_of_pent = [x for x in list_of_pent if str(x)[:2] in good_digits and str(x)[2:] in good_digits]
list_of_hex = [x for x in list_of_hex if str(x)[:2] in good_digits and str(x)[2:] in good_digits]
list_of_hept = [x for x in list_of_hept if str(x)[:2] in good_digits and str(x)[2:] in good_digits]
list_of_oct = [x for x in list_of_oct if str(x)[:2] in good_digits and str(x)[2:] in good_digits]

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


for tri_ in list_of_tri:
  for square_ in list_of_square:
    for pent_ in list_of_pent:
      for hex_ in list_of_hex:
        for hept_ in list_of_hept:
          for oct_ in list_of_oct:
            a = set([str(tri_)[:2], str(square_)[:2], str(pent_)[:2], str(hex_)[:2], str(hept_)[:2], str(oct_)[:2]])
            b = set([str(tri_)[2:], str(square_)[2:], str(pent_)[2:], str(hex_)[2:], str(hept_)[2:], str(oct_)[2:]])
            if len(a) == 6 and a == b:
              print(tri_, square_, pent_, hex_, hept_, oct_)