# Pretend universe has only 200, 100, 50, 20p coins
goal = 300 
num_ways = 0
num_200 = goal // 200
num_100 = goal // 100
num_50 = goal // 50
num_20 = goal // 20
num_10 = goal // 10
num_5 = goal // 5
num_2 = goal // 2
num_1 = goal // 1
for h in range(num_200, -1, -1):
  if h*200 <= goal:
    for j in range(num_100, -1, -1):
      if h*200 + j*100 <= goal:
        for k in range(num_50, -1, -1):
          if h*200 + j*100 + k*50 <= goal:
            for l in range(num_20, -1, -1):
              if h*200 + j*100 + k*50 + l*20 <= goal:
                for m in range(num_10, -1, -1):
                  if h*200 + j*100 + k*50 + l*20 + m*10 <= goal:
                    for n in range(num_5, -1, -1):
                      if h*200 + j*100 + k*50 + l*20 + m*10 + n*5 <= goal:
                        for o in range(num_2, -1, -1):
                          if h*200 + j*100 + k*50 + l*20 + m*10 + n*5 + 0*2 <= goal:
                            for p in range(num_1, -1, -1):
                              if h*200 + 100*j + 50*k + 20*l + 10*m + 5*n + 2*o + 1*p == goal:
                                num_ways += 1
                                print(f"Way {num_ways}: {h} 200p, {j} 100p, {k} 50p, {l} 20p, {m} 10p, {n} 5p, {o} 2p, {p} 1p")
