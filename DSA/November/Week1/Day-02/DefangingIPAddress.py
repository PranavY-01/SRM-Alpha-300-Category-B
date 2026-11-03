# DSA Daily Gym | November | Week 1 | Day 2 | Problem: 1108. Defanging an IP Address
# --------------------------------------------------------------------------------------
# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# Constraints:
# The given address is a valid IPv4 address.
# --------------------------------------------------------------------------------------

def defangIPaddr(address):
    result = ""

    for ch in address:
        if ch == '.':
            result += '[.]'
        else:
            result += ch

    return result

if __name__ == "__main__":
    # test cases
    address1 = "1.1.1.1"
    print(defangIPaddr(address1))  # Output: "1[.]1[.]1[.]1"

    address2 = "255.100.50.0"
    print(defangIPaddr(address2))  # Output: "255[.]100[.]50[.]0"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string address 
# Space Complexity: O(n), for the result string
# Pattern: String Traversal - Character Transformation
# --------------------------------------------------------------------------------------