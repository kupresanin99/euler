from math import log
my_list = []
my_max = 0
max_line_number = 0
line_number = 0
with open('099_data.txt', 'r') as f:
  for line in f:
  	my_list.append([i for i in line.strip('\n').split(",")])
for number in my_list:
  line_number += 1
  if int(number[1]) * log(int(number[0])) > my_max:
    my_max = int(number[1]) * log(int(number[0]))
    max_line_number = line_number
    print(f"New champion, line {line_number}")