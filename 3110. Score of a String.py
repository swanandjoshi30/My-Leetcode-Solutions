"""
You are given a string s. The score of a string is defined as 
the sum of the absolute difference between the ASCII values of adjacent characters.

Example:
Input: s = "hello"
Output: 13

Explanation:
The ASCII values of the characters in s are: 'h' = 104, 'e' = 101, 'l' = 108, 'o' = 111. 
So, the score of s would be |104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13.
"""

def scoreofstring(s) -> int:
    # Initialize the score counter
    count = 0
    
    # Iterate through the string from 0 to length-2
    for i in range(len(s) - 1):
        # Add the absolute difference between ASCII values of adjacent characters
        count += abs(ord(s[i]) - ord(s[i + 1]))
    
    # Return the final score
    return count