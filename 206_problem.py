mini = int(math.sqrt(1020304050607080900))
maxi = int(math.sqrt(1929394959697989990))

for i in range(mini + 20, maxi):
    if ((i*i%10 - i*i%1) / 1 == 0): 
        if ((i*i%1000 - i*i%100) / 100 == 9):
            if ((i*i%100000 - i*i%10000) / 10000 == 8):
                if ((i*i%10000000 - i*i%1000000) / 1000000 == 7):
                    if ((i*i%1000000000 - i*i%100000000) / 100000000 == 6):
                        if ((i*i%100000000000 - i*i%10000000000) / 10000000000 == 5):
                            if ((i*i%10000000000000 - i*i%1000000000000) / 1000000000000 == 4):
                                if ((i*i%1000000000000000 - i*i%100000000000000) / 100000000000000 == 3):
                                    if ((i*i%100000000000000000 - i*i%10000000000000000) / 10000000000000000 == 2):
                                        print(i*i, "   ", i)
