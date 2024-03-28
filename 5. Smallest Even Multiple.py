import math

class Solution:
  def smallest_even_multiple(self, n: int) -> int:
      lcm = (2 * n) // math.gcd(2, n)
      return lcm

