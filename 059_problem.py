from itertools import permutations
letters = "abcdefghijklmnopqrstuvwxyz"
list_of_pots = []
for pot in permutations(letters, 3):
  list_of_pots.append("".join(pot))

def make_binary(num):
  my_bin = ""
  int_num = int(num)
  for expo in range(7, -1, -1):
    if int_num // (2 ** expo) == 1: 
      my_bin += str(1)
      int_num -= 2 ** expo
    else: 
      my_bin += str(0)
  return my_bin

def xor(a, b):
  my_xor = ""
  for i in range(len(a)):
    if a[i] == b[i]:
      my_xor += "0"
    else:
      my_xor += "1"
  return my_xor

def get_letter(x):
  my_result = 0
  x = x[::-1]
  for m in range(8):
    my_result += int(x[m]) * (2 ** m)
  return chr(my_result)

my_list = []
with open('059_problem.txt', 'r') as f:
  for line in f:
  	my_list.append([i for i in line.strip('\n').split(",")])
my_list = my_list[0]

my_bins = []
for nums in my_list:
  my_bins.append(make_binary(nums))


for pots in list_of_pots:
  my_key = pots

  my_binary_key = []
  for letter in my_key:
    my_binary_key.append(make_binary(ord(letter)))
  my_binary_key = my_binary_key * int((len(my_bins) / len(my_binary_key)))

  my_zip = list(zip(my_bins, my_binary_key))

  answer = ""
  for tupe in my_zip:
    answer += get_letter(xor(tupe[0], tupe[1]))

  if 'the ' in answer or 'THE ' in answer:
    print(f"\n\n\nkey was {my_key}\n")
    print(answer)