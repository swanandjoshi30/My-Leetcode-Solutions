"""
You're given strings jewels representing the types of stones that are jewels, 
and stones representing the stones you have. Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels. 
Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
"""

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # Initialize a counter to keep track of jewels found in stones
        count = 0

        # Convert 'jewels' string into a set for O(1) lookup
        res = set(jewels)

        # Iterate over each stone in the 'stones' string
        for i in stones:
            # If the stone is a jewel, increment the counter
            if i in res:
                count += 1

        # Return the total count of jewels found in stones
        return count