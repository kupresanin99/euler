f = open('./022_problem.txt', 'r')
x = f.read().split(',')
f.close

import string
word_list = []
for word in x:
	word_list.append(''.join(x for x in word if x.isalpha()))
word_list = sorted(word_list)

counter = 0
big_sum = 0
for word in word_list:
    counter += 1
    word_count = 0
    for letter in word:
        #print(ord(letter) - 64)
        word_count += ord(letter) - 64
    #print(counter * word_count)
    big_sum += counter * word_count
    #print(word, big_sum)
print(big_sum)
