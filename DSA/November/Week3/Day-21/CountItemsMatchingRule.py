# DSA Daily Gym | November | Week 3 | Day 21 | Problem: 1773. Count Items Matching a Rule
# ----------------------------------------------------------------------------------------
# You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
# The ith item is said to match the rule if one of the following is true:
# - ruleKey == "type" and ruleValue == typei.
# - ruleKey == "color" and ruleValue == colori.
# - ruleKey == "name" and ruleValue == namei.
# Return the number of items that match the given rule.
# Constraints:
# 1 <= items.length <= 10^4
# 1 <= typei.length, colori.length, namei.length, ruleValue.length <= 10
# ruleKey is equal to either "type", "color", or "name".
# ----------------------------------------------------------------------------------------

def countMatches(items, ruleKey, ruleValue):
    key_index = {
        "type": 0,
        "color": 1,
        "name": 2
    }

    index = key_index[ruleKey]
    count = 0

    for item in items:
        if item[index] == ruleValue:
            count += 1

    return count

if __name__ == "__main__":
    # Test cases
    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "color"
    ruleValue = "silver"
    print(countMatches(items, ruleKey, ruleValue))  # Output: 1

    items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey = "type"
    ruleValue = "phone"
    print(countMatches(items, ruleKey, ruleValue))  # Output: 2

# ------------------------------------------------------------------------
# Time Complexity: O(n), where n is the number of items in the list.    
# Space Complexity: O(1), as we are using a constant amount of extra space.
# Pattern: Hash Map for Index Mapping
# ------------------------------------------------------------------------