file = open('018_problem.txt', 'r')
list_of_lists = []
line = file.readline()
while line:
  list_of_lists.append([int(x) for x in line.strip().split()])
  line = file.readline()
file.close()
list_of_bingos = []
rows = len(list_of_lists)
while rows >= 1:
  left_sum = sum([left[0] for left in list_of_lists])
  right_sum = sum([right[-1] for right in list_of_lists])
  list_of_bingos.append(list_of_lists[0][0])
  print(list_of_bingos)
  print(sum(list_of_bingos))
  
  if left_sum > right_sum:
    list_of_lists = [x[:-1] for x in list_of_lists]
  else: 
    list_of_lists = [x[1:] for x in list_of_lists]
  list_of_lists = list_of_lists[1:]
  rows = len(list_of_lists)