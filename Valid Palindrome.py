class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Check if a given string is a palindrome.

        Args:
            s (str): The input string.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        # Generate a clean string with only alphanumeric characters and in lowercase
        res_str = ''.join(char.lower() for char in s if char.isalnum())
        # Check if the clean string is equal to its reverse
        return res_str == res_str[::-1]
