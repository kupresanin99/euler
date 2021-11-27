my_list = []
my_sum = 0

with open('./013_problem.txt', 'r') as f:
  for line in f:
  	my_list.append(line.strip())

for number in my_list:
	my_sum += int(number)

print(str(my_sum)[:10])
