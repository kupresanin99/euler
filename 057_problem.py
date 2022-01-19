list_of_root_2 = 7 * [2]

counter = 1
N = 3
D = 2
print(f"Convergent {counter} has length of N: {len(str(N)):,.0f}, length of D: {len(str(D)):,.0f}")
bingos = 0
for i in range(1, 1000):
  counter += 1
  temp_N = N
  temp_D = D
  D = temp_N + temp_D
  N = 2 * temp_D + temp_N
  len_N = len(str(N))
  len_D = len(str(D))
  if len_N > len_D:
    bingos += 1
    print(f"Convergent {counter} has length of N: {len_N:,.0f}, length of D: {len_D:,.0f}")
print(bingos)