# DSA Daily Gym | November | Week 2 | Day 12 | Problem: 271. Encode and Decode Strings
# --------------------------------------------------------------------------------------
# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
# Implement the encode and decode methods.
# You are not allowed to use any built-in serialization methods, such as eval or serialize methods.
# Constraints:
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] contains any possible characters out of 256 valid ASCII characters.
# --------------------------------------------------------------------------------------

def encode(strs):
    result = ""

    for word in strs:
        result += str(len(word)) + "#" + word

    return result


def decode(s):
    result = []
    i = 0

    while i < len(s):  # Iterate through the encoded string - parse each string
        j = i

        while s[j] != "#":     
            j += 1

        length = int(s[i:j])  
        start = j + 1
        end = start + length

        result.append(s[start:end])  # Append the decoded string to the result list
        i = end

    return result

if __name__ == "__main__":
    # test cases
    strs1 = ["Hello", "World"]
    encoded1 = encode(strs1)
    print(encoded1)  # Output: "5#Hello5#World"
    decoded1 = decode(encoded1)
    print(decoded1)  # Output: ["Hello", "World"]

    strs2 = ["", "abc", "defg"]
    encoded2 = encode(strs2)
    print(encoded2)  # Output: "0#3#abc4#defg"
    decoded2 = decode(encoded2)
    print(decoded2)  # Output: ["", "abc", "defg"]

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the total number of characters in all strings combined.
# Space Complexity: O(n) for the encoded string and the decoded list of strings.
# Pattern: String Encoding and Decoding
# --------------------------------------------------------------------------------------