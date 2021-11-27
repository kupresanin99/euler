from collections import Counter
p1 = 0
p2 = 0
t = 0

def tiebreaker(hands):
	"""
	Takes a list of two 6-element lists
	Breaks poker hand ties, returns the winner
	"""
	
	# Break quad ties
	if hands[0][0] == 10:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		else:
			print("Player 2 wins")
			return 2

	# Break full house ties
	elif hands[0][0] == 9:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		else:
			print("Player 2 wins")
			return 2

	# Break flush ties
	elif hands[0][0] == 8:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		elif hands[0][1] < hands[1][1]:
			print("Player 2 wins")
			return 2
		else:
			if hands[0][2] > hands[1][2]:
				print("Player 1 wins")
				return 1
			elif hands[0][2] < hands[1][2]:
				print("Player 2 wins")
				return 2
			else:
				if hands[0][3] > hands[1][3]:
					print("Player 1 wins")
					return 1
				elif hands[0][3] < hands[1][3]:
					print("Player 2 wins")
					return 2
				else:
					if hands[0][4] > hands[1][4]:
						print("Player 1 wins")
						return 1
					elif hands[0][4] < hands[1][4]:
						print("Player 2 wins")
						return 2
					else:
						if hands[0][5] > hands[1][5]:
							print("Player 1 wins")
							return 1
						elif hands[0][5] < hands[1][5]:
							print("Player 2 wins")
							return 2
						else:
							print("WHAT THE FUCKIO")


	# Break straight ties
	elif hands[0][0] == 7:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		elif hands[0][1] < hands[1][1]:
			print("Player 2 wins")
			return 2
		else:
			print("WHAT THE FUCKO")


	# Break trips ties
	elif hands[0][0] == 6:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		else:
			print("Player 2 wins")
			return 2

	# Break two-pair ties
	elif hands[0][0] == 5:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		elif hands[0][1] < hands[1][1]:
			print("Player 2 wins")
			return 2
		else:
			if hands[0][2] > hands[1][2]:
				print("Player 1 wins")
				return 1
			elif hands[0][2] < hands[1][2]:
				print("Player 2 wins")
				return 2
			else:
				if hands[0][3] > hands[1][3]:
					print("Player 1 wins")
					return 1
				elif hands[0][3] < hands[1][3]:
					print("Player 2 wins")
					return 2
				else:
					print("WHAT THE FUCKO")

	# Break one-pair ties
	elif hands[0][0] == 4:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		elif hands[0][1] < hands[1][1]:
			print("Player 2 wins")
			return 2
		else:
			if hands[0][2] > hands[1][2]:
				print("Player 1 wins")
				return 1
			elif hands[0][2] < hands[1][2]:
				print("Player 2 wins")
				return 2
			else:
				if hands[0][3] > hands[1][3]:
					print("Player 1 wins")
					return 1
				elif hands[0][3] < hands[1][3]:
					print("Player 2 wins")
					return 2
				else:
					if hands[0][4] > hands[1][4]:
						print("Player 1 wins")
						return 1
					elif hands[0][4] < hands[1][4]:
						print("Player 2 wins")
						return 2
					else:
						print("WHAT THE FUCKIIOIOOOIO??")

	# Break no-pair ties
	elif hands[0][0] == 3:
		if hands[0][1] > hands[1][1]:
			print("Player 1 wins")
			return 1
		elif hands[0][1] < hands[1][1]:
			print("Player 2 wins")
			return 2
		else:
			if hands[0][2] > hands[1][2]:
				print("Player 1 wins")
				return 1
			elif hands[0][2] < hands[1][2]:
				print("Player 2 wins")
				return 2
			else:
				if hands[0][3] > hands[1][3]:
					print("Player 1 wins")
					return 1
				elif hands[0][3] < hands[1][3]:
					print("Player 2 wins")
					return 2
				else:
					if hands[0][4] > hands[1][4]:
						print("Player 1 wins")
						return 1
					elif hands[0][4] < hands[1][4]:
						print("Player 2 wins")
						return 2
					else:
						if hands[0][5] > hands[1][5]:
							print("Player 1 wins")
							return 1
						elif hands[0][5] < hands[1][5]:
							print("Player 2 wins")
							return 2
						else:
							print("WHAT THE FUCKIO")

	else:
		print("WHAT THE FUCKO?")

	return 0

def four_finder(hand):
	"""
	Takes a 5-card hand, concats, only takes ranks
	If we get 4 of a kind, return list:
	[10, quad rank, 0, 0, 0, 0]
	"""
	cards = ''.join(hand)[::2]
	if Counter(cards).most_common(1)[0][1] == 4:
		return [10, Counter(cards).most_common(1)[0][0], 0, 0, 0, 0]
	else:
		return [0, 0, 0, 0, 0, 0]

def full_finder(hand):
	"""
	Takes a 5-card hand, concats, only takes ranks
	If we get 3 of a kind and also a pair, return list:
	[9, trip rank, 0, 0, 0, 0]
	"""
	cards = ''.join(hand)[::2]
	if Counter(cards).most_common(1)[0][1] == 3:
		if Counter(cards).most_common(2)[1][1] == 2:
			return [9, Counter(cards).most_common(1)[0][0], 0, 0, 0, 0]
		else:
			return [0, 0, 0, 0, 0, 0]
	else:
		return [0, 0, 0, 0, 0, 0]

def flush_finder(hand):
	"""
	Takes a 5-card hand, concats, returns the most frequent symbol.
	If we get 5 matching suits, we have a flush, return list:
	[8, high card rank, 2nd rank, 3rd rank, 4th rank, 5th rank]
	"""
	suits = ''.join(hand)
	if Counter(suits).most_common(1)[0][1] == 5:
		cards = ''.join(hand)[::2]
		ranks = sorted(cards, reverse=True)
		return [8, ord(ranks[0]), ord(ranks[1]), ord(ranks[2]), ord(ranks[3]), ord(ranks[4])]
	else:
		return [0, 0, 0, 0, 0, 0]

def straight_finder(hand):
	"""
	Takes a 5-card hand, concats, only takes ranks
	If we get a straight, return list:
	[7, high card rank, 0, 0, 0, 0]
	"""
	if Counter(''.join(hand)[::2]).most_common(1)[0][1] == 1:
		max = 50
		min = 62
		for letter in ''.join(hand)[::2]:
			if ord(letter) > max:
				max = ord(letter)
			if ord(letter) < min:
				min = ord(letter)
		if max - min == 4:
			return [7, max, 0, 0, 0, 0]
		else:
			return [0, 0, 0, 0, 0, 0]
	else:
		return [0, 0, 0, 0, 0, 0]

def trip_finder(hand):
	"""
	Takes a 5-card hand, concats, only takes ranks
	If we get 3 of a kind only, returns list:
	[6, trip rank, 0, 0, 0, 0]
	"""
	cards = ''.join(hand)[::2]
	if Counter(cards).most_common(1)[0][1] == 3:
		if Counter(cards).most_common(2)[1][1] == 1:
			return [6, Counter(cards).most_common(1)[0][0], 0, 0, 0, 0]
		else:
			return [0, 0, 0, 0, 0, 0]
	else:
		return [0, 0, 0, 0, 0, 0]

def two_pair_finder(hand):
	"""
	Takes a 5-card hand, concats, only takes ranks
	If we get 2 pair, returns list:
	[5, top pair rank, second pair rank, fifth card, 0, 0]
	"""
	cards = ''.join(hand)[::2]
	if Counter(cards).most_common(3)[0][1] == 2:
		if Counter(cards).most_common(3)[1][1] == 2:
			temp1 = Counter(cards).most_common(3)[0][0]
			temp2 = Counter(cards).most_common(3)[1][0]
			top = max(temp1, temp2)
			second = min(temp1, temp2)
			kicker = Counter(cards).most_common(3)[2][0]
			return [5, top, second, kicker, 0, 0]
		else:
			return [0, 0, 0, 0, 0, 0]
	else:
		return [0, 0, 0, 0, 0, 0]

def one_pair_finder(hand):
	"""
	Takes a 5-card hand, concats, only takes ranks
	If we get 1 pair, returns list:
	[4, pair rank, kicker1, kicker2, kicker3]
	"""
	cards = ''.join(hand)[::2]
	if Counter(cards).most_common(4)[0][1] == 2:
		if Counter(cards).most_common(4)[1][1] == 1:
			pair = Counter(cards).most_common(4)[0][0]
			temp1 = Counter(cards).most_common(4)[1][0]
			temp2 = Counter(cards).most_common(4)[2][0]
			temp3 = Counter(cards).most_common(4)[3][0]
			ranks = sorted([temp1, temp2, temp3], reverse=True)
			return [4, pair, ord(ranks[0]), ord(ranks[1]), ord(ranks[2]), 0]
		else:
			return [0, 0, 0, 0, 0, 0]
	else:
		return [0, 0, 0, 0, 0, 0]

def no_pair_finder(hand):
	"""
	Takes a 5-card hand, concats, only takes ranks
	If we get no pair, returns list:
	[3, max, 2nd, 3rd, 4th, min]
	"""
	cards = ''.join(hand)[::2]
	if Counter(cards).most_common(1)[0][1] == 1:
		ranks = sorted(cards, reverse=True)
		return [3, ord(ranks[0]), ord(ranks[1]), ord(ranks[2]), ord(ranks[3]), ord(ranks[4])]
	else:
		return [0, 0, 0, 0, 0, 0] 


my_list = []

with open('./054_problem.txt', 'r') as f:
  for line in f:
  	my_list.append(line.strip('\n').split(" "))

coded_list = []
for hand in my_list:
	coded_hand = []
	for card in hand:
		coded_hand.append(card.replace("T", ":").replace("J", ";").replace("Q", "<").replace("K", "=").replace("A", ">"))
	coded_list.append(coded_hand)

split_list  =[]
for hand in coded_list:
	first_hand = hand[:5]
	second_hand = hand[5:]
	temp_hand = []
	temp_hand.append(first_hand)
	temp_hand.append(second_hand)
	split_list.append(temp_hand)

printer_list  =[]
for hand in my_list:
	first_hand = hand[:5]
	second_hand = hand[5:]
	temp_hand = []
	temp_hand.append(first_hand)
	temp_hand.append(second_hand)
	printer_list.append(temp_hand)

for game in range(len(split_list)):
	results = [[], []]
	for hand in range(2):

		if four_finder(split_list[game][hand])[0] == 10:
			results[hand] = four_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has a four of kind')

		elif full_finder(split_list[game][hand])[0] == 9:
			results[hand] = full_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has a full house')

		elif flush_finder(split_list[game][hand])[0] == 8:
			results[hand] = flush_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has a flush')

		elif straight_finder(split_list[game][hand])[0] == 7:
			results[hand] = straight_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has a straight')

		elif trip_finder(split_list[game][hand])[0] == 6:
			results[hand] = trip_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has trips')

		elif two_pair_finder(split_list[game][hand])[0] == 5:
			results[hand] = two_pair_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has a two-pair')

		elif one_pair_finder(split_list[game][hand])[0] == 4:
			results[hand] = one_pair_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has a one-pair')

		elif no_pair_finder(split_list[game][hand])[0] == 3:
			results[hand] = no_pair_finder(split_list[game][hand])
			print('Game', game, 'Hand', hand, '=', printer_list[game][hand], 'has a no pair')

		else: 
			print("WHAT THE FUCKO?")

	if results[0][0] > results[1][0]:
		print("Player 1 wins")
		p1 += 1
	elif results[0][0] < results[1][0]:
		print("Player 2 wins")
		p2 += 1
	else:
		tie_winner = tiebreaker(results)
		if tie_winner == 1:
			p1 += 1
		elif tie_winner == 2:
			p2 += 1
		else: 
			print("WHAT THE SERIOUS FUCK?")

	print('\n\n')

print("Player 1 wins", p1)
print("Player 2 wins", p2)


































