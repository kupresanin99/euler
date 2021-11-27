my_list = []

with open('./011_problem.txt', 'r') as f:
  for line in f:
  	my_list.append([int(i) for i in line.strip('\n').split(" ")])

row_max = 0

for row in my_list:
	for q in range(17):
		producto = row[q + 0] * row[q + 1] * row[q + 2] * row[q + 3]
		if producto > row_max:
			row_max = producto

print(row_max)

column_max = 0

for i in range(20):
	for j in range(17):
		producto = my_list[j + 0][i] * my_list[j + 1][i] * my_list[j + 2][i] * my_list[j + 3][i]
		if producto > column_max:
			column_max = producto

print(column_max)

diag_1_max = 0

for row in range(17):
	for col in range(17):
		try:
			producto = my_list[row + 0][col + 0] * my_list[row + 1][col + 1] * my_list[row + 2][col + 2] * my_list[row + 3][col + 3]
		except:
			pass
		if producto > diag_1_max:
			diag_1_max = producto

print(diag_1_max)

diag_2_max = 0

for row in range(3,20):
	for col in range(17):
		try:
			producto = my_list[row - 0][col + 0] * my_list[row - 1][col + 1] * my_list[row - 2][col + 2] * my_list[row - 3][col + 3]
		except:
			pass
		if producto > diag_2_max:
			diag_2_max = producto

print(diag_2_max)