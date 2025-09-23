"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.
A defanged IP address replaces every period "." with "[.]".

Example:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""

# Method 1: Using built-in string function
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Use the replace() method to replace every "." with "[.]"
        return address.replace(".", "[.]")



# Method 2: Without using built-in replace()
class Solution:
    def defangIPaddr(self, address: str) -> str:
        # Initialize an empty string to build the defanged IP
        result = ""
        
        # Iterate through each character in the input address
        for i in address:
            # If the character is ".", append "[.]" to the result
            if i == ".":
                result += "[.]"
            # Otherwise, append the character itself
            else:
                result += i
        
        # Return the final defanged IP address
        return result

  # Output: "1[.]1[.]1[.]1"
