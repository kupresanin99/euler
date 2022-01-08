# From problem, we believe there exists an answer greater than 918,273,645 
# From trial and error....
# We believe must be of the form YYYY * 1 and then YYYYY * 2 to give YYY,YZZ,ZZZ as a 9-digit answer.
# So only need to check from 9,183 up to 9,876 

list_of_possible_answers = []
list_of_pandigital_answers = []

for num in range(9183, 9876):
  list_of_possible_answers.append(str(num) + str(2 * num))

for num in list_of_possible_answers:
  if ''.join(sorted(num)) == '123456789':
    list_of_pandigital_answers.append(num)
answer = max(list_of_pandigital_answers)
print(f"\n{answer} = {answer[:4]} CONCAT WITH 2 * {answer[:4]} = {2 * int(answer[:4]):}\n")