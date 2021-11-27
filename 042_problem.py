f = open('./042_problem.txt', 'r')
x = f.read().split(',')
f.close

import string
word_list = []
for word in x:
	word_list.append(''.join(x for x in word if x.isalpha()))

value_list = []
for word in word_list:
	sum_count = 0
	for letter in word:
		sum_count += (ord(letter) - 64)
	value_list.append(sum_count)

tri_list = []
for i in range(20):
	tri_list.append(int(0.5 * i * (i + 1)))

count = 0
for value in value_list:
	if value in tri_list:
		count += 1

print("count =", count)
