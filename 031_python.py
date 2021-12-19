# Pretend universe has only 200, 100, 50, 20p coins
goal = 200 
num_ways = 1
num_100 = goal // 100
num_50 = goal // 50
num_20 = goal // 20
num_10 = goal // 10
num_5 = goal // 5
num_2 = goal // 2
num_1 = goal // 1
for j in range(num_100, -1, -1):
  for k in range(num_50, -1, -1):
    for l in range(num_20, -1, -1):
      for m in range(num_10, -1, -1):
        for n in range(num_5, -1, -1):
          for o in range(num_2, -1, -1):
            for p in range(num_1, -1, -1):
              if 100*j + 50*k + 20*l + 10*m + 5*n + 2*o + 1*p == 200:
                num_ways += 1
                print(f"Way {num_ways}: {j} 100p, {k} 50p, {l} 20p, {m} 10p, {n} 5p, {o} 2p, {p} 1p")