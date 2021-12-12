f1 = 1
f2 = 1
index = 2
digits = 1
while digits < 1000:
  index += 1
  current = f1 + f2
  f1 = f2
  f2 = current
  digits = len(str(f2))
print(f"index = {index} has digits = {digits}")
print(f"That fib = {f2:,}")