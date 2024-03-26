class Solution:
    def isPalindrome(self, x: int) -> bool:
    # Check if x is negative or if it ends with a zero (excluding zero itself)
      if x < 0 or (x != 0 and x % 10 == 0):
          return False
      
      reversed_num = 0
      original_x = x
      
      # Reverse the integer
      while x > 0:
          digit = x % 10
          reversed_num = reversed_num * 10 + digit
          x //= 10
      
      # Compare the reversed number with the original
      return original_x == reversed_num

