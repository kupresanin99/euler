
file = open('018_problem.txt', 'r')
list_of_lists = []
line = file.readline()
longest_line = 0
while line:
  longest_line += 1
  list_of_lists.append([int(x) for x in line.strip().split()])
  line = file.readline()
file.close()

for my_item in list_of_lists:
  for j in range(longest_line - len(my_item)):
    my_item.append(0)
list_of_lists = list_of_lists[::-1]
my_sum = [0] * len(list_of_lists)

for i in range(1, len(list_of_lists)):
  if i == 1:
    bottom = list_of_lists[0]
    top = list_of_lists[1]
  else:
    bottom = my_sum
    top = list_of_lists[i]
  j = 0
  print(f"top = {top}")
  print(f"bottom = {bottom}")
  for num in top:
    print(f"num = {num}")
    if num != 0:
      print(f"max = {max(num + bottom[j], num + bottom[j + 1])}")
      my_sum[j] = max(num + bottom[j], num + bottom[j + 1])
      j += 1
      print(my_sum)
  
  