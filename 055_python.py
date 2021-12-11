lychrel_counter = 0
for num in range(10000):
  current_num = num
  reversed_string = str(num)[::-1]
  reversed_num = int(reversed_string)
  current_sum = num + reversed_num
  palindrome = False
  iteration = 1
  while not palindrome and iteration < 50:
    if str(current_sum) == str(current_sum)[::-1]:
      palindrome = True
    else:
        iteration += 1
        
        if iteration == 50:
          lychrel_counter += 1
          print(f"We have found {num} to be Lychrel number {lychrel_counter}")
        else:
          current_num = current_sum
          reversed_string = str(current_num)[::-1]
          reversed_num = int(reversed_string)
          current_sum = current_num + reversed_num

print(f"\nWe have found {lychrel_counter} Lychrel numbers")
