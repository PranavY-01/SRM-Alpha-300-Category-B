# DSA Daily Gym | November | Week 3 | Day 21 | Problem: 2047. Valid Words in a Sentence
# ----------------------------------------------------------------------------------------
# A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.
# A token is a valid word if all the following are true:
# - It only contains lowercase letters, hyphens, and/or punctuation (no digits).
# - There is at most one hyphen '-'. If present, it should be surrounded by lowercase characters (i.e., not at the start or end).
# - There is at most one punctuation mark. If present, it should be at the end of the token.
# Given a string sentence, return the number of valid words in it.
# Constraints:
# 1 <= sentence.length <= 1000
# sentence consists of lowercase letters, digits, hyphens, punctuation marks, and spaces.
# ----------------------------------------------------------------------------------------

def countWords(s):
    count = 0
    inside_word = False

    for ch in s:
        if ch.isspace():
            inside_word = False

        else:
            if not inside_word:
                count += 1

            inside_word = True

    return count

if __name__ == "__main__":
    # Test cases
    sentence = "cat and  dog"
    print(countWords(sentence))  # Output: 3

    sentence = "!this  1-s b8d!"
    print(countWords(sentence))  # Output: 0

    sentence = "alice and  bob are playing stone-game10"
    print(countWords(sentence))  # Output: 5

# ------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the sentence.
# Space Complexity: O(1), as we are using a constant amount of extra space.
# Pattern: String Traversal and Counting
# ------------------------------------------------------------------------