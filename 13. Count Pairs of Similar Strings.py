from typing import List
from collections import Counter

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # Initialize the number of similar pairs to zero
        similar_pairs_count = 0
      
        # Initialize a Counter to keep track of the different bit patterns
        bit_pattern_counter = Counter()
      
        # Iterate through each word in the list
        for word in words:
            # Start with a bit vector of 0 for each word
            bit_vector = 0
          
            # Iterate through each character in the word
            for char in word:
                # Shift 1 to the left by the position of the character in the alphabet
                # 'A' would correspond to bit 0, 'B' to bit 1, and so on.
                bit_vector |= 1 << (ord(char) - ord('A'))
          
            # Add the current bit vector pattern's existing count to similar_pairs_count
            similar_pairs_count += bit_pattern_counter[bit_vector]
          
            # Increment the count for this bit pattern in the counter
            bit_pattern_counter[bit_vector] += 1
      
        # Return the total count of similar pairs
        return similar_pairs_count
