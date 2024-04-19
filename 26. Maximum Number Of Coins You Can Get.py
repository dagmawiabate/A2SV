from typing import List

class Solution:
  def maxCoins(self, piles: List[int]) -> int:  
    # Sort the piles in descending order piles. 
    sort(reverse=True) # [8, 7, 4, 2, 2, 1]
    #3 1
    #6 2
    #9 3
    # Initialize variables
    coins = 0
    i = 1

    # Iterate through the piles, picking every second pile
    while i < ((len(piles)) - (len(piles) / 3)): 
      coins += piles[i]
      i += 2

    return coins