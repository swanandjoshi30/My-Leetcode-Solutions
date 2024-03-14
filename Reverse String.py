class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
# Initialize two pointers, one at the beginning and one at the end of the list
        i = 0
        j = len(s) - 1
        
        # Iterate until the two pointers meet
        while i < j:
            # Swap the characters at positions i and j
            s[i], s[j] = s[j], s[i]
            # Move the pointers towards each other
            i += 1
            j -= 1
