m = 20
n = 20
# Lattice paths in SE direction have m + n choose m

from math import factorial

lat_paths = factorial(40) / (factorial(20) * factorial(20))
print(lat_paths)