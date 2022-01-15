# Pretty sure answers must start with 10 - 16 so that 1X, 2X, 3X, 4X, 5X, 6X all retain same number of digits
digits = [1, 2, 3, 4]
for digit in digits:
  for i in range(10, 17):
    for j in range(0, 10 ** digit):
      my_string = str(i) + str(j).zfill(digit)
      my_int = int(my_string)
      x2 = "".join(sorted(str(2 * my_int)))
      x3 = "".join(sorted(str(3 * my_int)))
      x4 = "".join(sorted(str(4 * my_int)))
      x5 = "".join(sorted(str(5 * my_int)))
      x6 = "".join(sorted(str(6 * my_int)))
      if len(x6) == len(x5):
        if len({x2, x3, x4, x5, x6}) == 1:
          print(f"""my_string: {my_string}, x2: {x2}, x3: {x3}, x4: {x4}, x5: {x5} x6: {x6}""")