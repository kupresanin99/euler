max_num = 0
max_count = 0
for p in range(1000, 12, -1):
  my_count = 0
  for c in range(round(0.4 * p) + 1, round(0.5 * p)):
    remainder = p - c
    for b in range(1, int(remainder / 2 + 1)):
      a = p - c - b
      if a < c and b < c and a * a + b * b == c * c:
        my_count += 1
        print(f"p={p}, c={c}, b={b}, a={a}")
  if my_count > max_count:
    max_num = p
    max_count = my_count
print(f"max_num = {max_num} with max_count = {max_count}")