# DSA Daily Gym | November | Week 1 | Day 1 | Problem: 38. Count and Say
# --------------------------------------------------------------------------------------
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
# countAndSay(1) = "1"
# countAndSay(n) is the run-length encoding of countAndSay(n - 1).
# Given a positive integer n, return the nth element of the count-and-say sequence.
# Constraints:
# 1 <= n <= 30
# --------------------------------------------------------------------------------------

def countAndSay(n):
    result = "1"

    for _ in range(n - 1):
        next_result = ""
        i = 0

        while i < len(result):
            count = 1

            # Count consecutive identical digits
            while i + 1 < len(result) and result[i] == result[i + 1]:
                count += 1
                i += 1

            # Append count and digit
            next_result += str(count) + result[i]
            i += 1

        result = next_result

    return result

if __name__ == "__main__":
    # test cases
    n1 = 1
    print(countAndSay(n1))  # Output: "1"

    n2 = 4
    print(countAndSay(n2))  # Output: "1211"

    n3 = 5
    print(countAndSay(n3))  # Output: "111221"

# --------------------------------------------------------------------------------------
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Pattern: String Traversal - Run Length Encoding
# --------------------------------------------------------------------------------------