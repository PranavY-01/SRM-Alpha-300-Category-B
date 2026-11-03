# DSA Daily Gym | November | Week 1 | Day 2 | Problem: 2129. Capitalize the Title
# --------------------------------------------------------------------------------------
# You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters.
# Capitalize the string by changing the capitalization of each word such that:
# If the length of the word is 1 or 2 letters, change all letters to lowercase.
# Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
# Return the capitalized title.
# Constraints:
# 1 <= title.length <= 100
# title consists of words separated by a single space without any leading or trailing spaces.
# --------------------------------------------------------------------------------------

def capitalizeTitle(title):
    def to_lower(ch):
        if 'A' <= ch <= 'Z':
            return chr(ord(ch) + 32)
        return ch

    def to_upper(ch):
        if 'a' <= ch <= 'z':
            return chr(ord(ch) - 32)
        return ch

    words = title.split()
    result = []

    for word in words:

        if len(word) < 3:
            new_word = ""

            for ch in word:
                new_word += to_lower(ch)

        else:
            new_word = to_upper(to_lower(word[0]))

            for i in range(1, len(word)):
                new_word += to_lower(word[i])

        result.append(new_word)

    return " ".join(result)

if __name__ == "__main__":
    # test cases
    title1 = "capiTalIze tHe titLe"
    print(capitalizeTitle(title1))  # Output: "Capitalize The Title"

    title2 = "First leTTeR of EACH Word"
    print(capitalizeTitle(title2))  # Output: "First Letter of Each Word"

    title3 = "i lOve leetcode"
    print(capitalizeTitle(title3))  # Output: "i Love Leetcode"

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the string title
# Space Complexity: O(n), for the result string
# Pattern: String Traversal - Word Capitalization
# --------------------------------------------------------------------------------------