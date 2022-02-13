stopper = 1
max_counter = 0
max_answer = 0
for num in range(2, 1000001):
	temp_num = num
	counter = 1
	while num > stopper:
		counter += 1
		if num % 2 == 0:
			num = int(num / 2)
		elif num % 2 != 0:
			num = int(3 * num + 1)
	if counter > max_counter:
		max_counter = counter
		max_answer = temp_num
		print("New Record: Number", temp_num, "needs", counter, "steps.")

print("\n\nThe winning number is", max_answer, "with", max_counter, "steps.\n\n")

