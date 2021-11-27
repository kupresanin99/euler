ld = {1:"one",
     2:"two",
     3:"three",
     4:"four", 
     5:"five",
     6:"six",
     7:"seven",
     8:"eight",
     9:"nine",
     10:"ten",
     11:"eleven",
     12:"twelve", 
     13:"thirteen",
     14:"fourteen",
     15:"fifteen",
     16:"sixteen",
     17:"seventeen",
     18:"eighteen",
     19:"nineteen",
     20:"twenty",
     30:"thirty",
     40:"forty",
     50:"fifty",
     60:"sixty",
     70:"seventy",
     80:"eighty",
     90:"ninety",
     100:"hundred",
     1000:"thousand"}

overall_sum = 0
count = 0
for i in range(1,21):
    overall_sum += len(ld[i])
    count += 1

for j in range(21, 100):
    if j%10 != 0:
        overall_sum += len(ld[10*(j//10)]) + len(ld[j%10])
    if j%10 == 0:
        overall_sum += len(ld[10*(j//10)])
    count += 1

new_sum = overall_sum
for k in range(1, 10):
    new_sum += overall_sum + 99 * (len(ld[k]) + len(ld[100]) + len("and"))

for k in range(1, 10):
    new_sum += len(ld[k]) + len(ld[100])

new_sum += len("onethousand")

print(new_sum)
