"""
You are given a 0-indexed array of strings 'words' and a character 'x'.
Return an array of indices representing the words that contain the character 'x'.
The returned array can be in any order.

Example:
Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet" and "code". Hence, we return indices 0 and 1.
"""

from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Initialize an empty list to store the indices of words containing 'x'
        l1 = []

        # Iterate over the indices of the 'words' list
        for i in range(len(words)):
            # Check if character 'x' is present in the current word
            if x in words[i]:
                # If yes, append the index to the result list
                l1.append(i)
        
        # Return the list of indices
        return l1