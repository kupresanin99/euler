from itertools import permutations
my_sum = 0
perm = list(permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

for num in perm:
  temp = ''.join([str(x) for x in num])
  if int(temp[1:4]) % 2 == 0:
    if int(temp[2:5]) % 3 == 0:
      if int(temp[3:6]) % 5 == 0:
        if int(temp[4:7]) % 7 == 0:
          if int(temp[5:8]) % 11 == 0:
            if int(temp[6:9]) % 13 == 0:
              if int(temp[7:10]) % 17 == 0: 
                print(temp)
                my_sum += int(temp)
print(f"\nThe sum is {my_sum}")
