import random
counter = 0
my_sum = 0
for i in range(10000000):
  counter += 1
  my_cards = list(range(1, 53))
  random.shuffle(my_cards)
  my_pairs = [abs(j - i) % 13 for i, j in zip(my_cards[:-1], my_cards[1:])]
  try:
    first_pair = my_pairs.index(0) + 2
  except ValueError:
    first_pair = 52
  my_sum += first_pair
  my_average = my_sum / counter
  print(my_average)