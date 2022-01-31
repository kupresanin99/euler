my_list = []

with open('./089_problem.txt', 'r') as f:
  for line in f:
  	my_list.append(line.strip('\n'))

roman = {'M': 1000,
        'D': 500, 
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1,
        'P': 4, 
        'Q': 9,
        'R': 40,
        'S': 90,
        'T': 400,
        'U': 900}

def four_finder(numeral):
    if 'IV' in numeral:
        return numeral.index('IV')

def nine_finder(numeral):
    if 'IX' in numeral:
        return numeral.index('IX')
    
def forty_finder(numeral):
    if 'XL' in numeral:
        return numeral.index('XL')
    
def ninety_finder(numeral):
    if 'XC' in numeral:
        return numeral.index('XC')
    
def four_hundred_finder(numeral):
    if 'CD' in numeral:
        return numeral.index('CD')
    
def nine_hundred_finder(numeral):
    if 'CM' in numeral:
        return numeral.index('CM')

char_count = 0
values = []
for numeral in my_list:
    new = numeral
    al = []
    
    if nine_hundred_finder(numeral) is not None:
        new = new.replace("CM", "U")
    if four_hundred_finder(numeral) is not None:
        new = new.replace("CD", "T")
    if ninety_finder(numeral) is not None:
        new = new.replace("XC", "S")
    if forty_finder(numeral) is not None:
        new = new.replace("XL", "R")
    if nine_finder(numeral) is not None:
        new = new.replace("IX", "Q")    
    if four_finder(numeral) is not None:
        new = new.replace("IV", "P")
    roman_value = 0
    for letter in new:
        roman_value += roman[letter]
    char_count += len(numeral)
    values.append(roman_value)

def to_roman(num):
    the_roman = []
    the_roman.append(num // 1000 * "M")
    num = num % 1000
    the_roman.append(num // 900 * "CM")
    num = num % 900
    the_roman.append(num//500 * "D")
    num = num%500
    the_roman.append(num//400 * "CD")
    num = num%400
    the_roman.append(num//100 * "C")
    num = num%100
    the_roman.append(num//90 * "XC")
    num = num%90
    the_roman.append(num//50 * "L")
    num = num%50
    the_roman.append(num//40 * "XL")
    num = num%40
    the_roman.append(num//10 * "X")
    num = num%10
    the_roman.append(num//9 * "IX")
    num = num%9
    the_roman.append(num//5 * "V")
    num = num%5
    the_roman.append(num//4 * "IV")
    num = num%4
    the_roman.append(num//1 * "I")
    num = num%1
    return len(''.join(the_roman))

shorter_sum = 0
for value in values:
    shorter_sum += to_roman(value)

print(char_count - shorter_sum)
