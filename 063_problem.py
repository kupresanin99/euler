counter = 0
for exponent in range(1, 1000):
  for base in range(1, 100):
    if exponent == len(str(base ** exponent)):
      counter += 1
      print(f"Got #{counter}: {base} to the {exponent} = {base ** exponent:,.0f} with {len(str(base ** exponent))} digits")