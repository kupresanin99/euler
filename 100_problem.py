from math import sqrt
current_b = 15
current_r = 6
current_sum_ratio = current_b / current_r
current_sum = current_b + current_r
next_ish_b = 80

while current_sum <= 1000000000000:
  for b in range(next_ish_b, 1000000000000):
    r = int(b // (1 + sqrt(2)))
    my_answer = (2*b*b-2*b)/(b*b+r*r+2*b*r-b-r)
    if my_answer == 1:
      this_sum = b + r
      current_sum_ratio = this_sum / current_sum
      current_sum = this_sum
      next_ish_b = int(current_sum_ratio * b)
      print(f"b={b:,}, r={r:,}, sum={this_sum:,}, nextish_b={next_ish_b:,.0f}")
      break
