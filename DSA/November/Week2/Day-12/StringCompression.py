# DSA Daily Gym | November | Week 2 | Day 12 | Problem: 443. String Compression
# --------------------------------------------------------------------------------------
# Given an array of characters chars, compress it using the following algorithm:
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
# 1. If the group's length is 1, append the character to s.
# 2. Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars.
# Note that group lengths that are 10 or longer will be split into multiple characters in chars.
# After you are done modifying the input array, return the new length of the array.
# You must write an algorithm that uses only constant extra space.
# Constraints:
# 1 <= chars.length <= 2000
# chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
# --------------------------------------------------------------------------------------

def compress(chars):
    read = 0
    write = 0
    n = len(chars)

    while read < n:
        current = chars[read]
        count = 0

        while read < n and chars[read] == current:
            count += 1
            read += 1

        chars[write] = current
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write

if __name__ == "__main__":
    # test cases
    chars1 = ["a", "a", "b", "b", "c", "c", "c"]
    new_length1 = compress(chars1)
    print(new_length1)  # Output: 6
    print(chars1[:new_length1])  # Output: ['a', '2', 'b', '2', 'c', '3']

    chars2 = ["a"]
    new_length2 = compress(chars2)
    print(new_length2)  # Output: 1
    print(chars2[:new_length2])  # Output: ['a']

    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    new_length3 = compress(chars3)
    print(new_length3)  # Output: 4
    print(chars3[:new_length3])  # Output: ['a', 'b', '1', '2']