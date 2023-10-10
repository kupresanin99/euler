base = 290797
mod = 50515093
n1 = base
n2 = (base * base) % mod
my_list = [(n1, n2)]
min_distance = 999888777666
for i in range(10000):
  n1 = (n2 * n2) % mod
  n2 = (n1 * n1) % mod
  my_list.append((n1, n2))
for i in range(len(my_list) - 1):
  for j in range(i + 1, len(my_list)):
    temp_value = ((my_list[i][0] - my_list[j][0]) ** 2 + (my_list[i][1] - my_list[j][1]) ** 2) ** 0.5
    if temp_value <= min_distance:
      min_distance = temp_value
      print(i, j, my_list[i], my_list[j], ((my_list[i][0] - my_list[j][0]) ** 2 + (my_list[i][1] - my_list[j][1]) ** 2) ** 0.5, min_distance)
