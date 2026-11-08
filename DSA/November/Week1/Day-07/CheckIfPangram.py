# DSA Daily Gym | November | Week 1 | Day 7 | Problem: 1832. Check if the Sentence Is Pangram
# --------------------------------------------------------------------------------------
# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
# Constraints:  
# 1 <= sentence.length <= 1000
# sentence consists of lowercase English letters.   
# --------------------------------------------------------------------------------------

def checkIfPangram(sentence):
    seen = set()

    for ch in sentence:
        if 'a' <= ch <= 'z':
            seen.add(ch)

    return len(seen) == 26

if __name__ == "__main__":
    # test cases
    sentence1 = "thequickbrownfoxjumpsoverthelazydog"
    print(checkIfPangram(sentence1))  # Output: True

    sentence2 = "leetcode"
    print(checkIfPangram(sentence2))  # Output: False

# --------------------------------------------------------------------------------------
# Time Complexity: O(n), where n is the length of the sentence. We iterate through the sentence once to create a set of unique characters.
# Space Complexity: O(1), since the size of the alphabet set is constant (26 letters), and the space used for the sentence set is at most 26 as well.
# Pattern: Hashing, Set
# --------------------------------------------------------------------------------------