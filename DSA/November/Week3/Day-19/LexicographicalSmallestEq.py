# DSA Daily Gym | November | Week 3 | Day 19 | Problem: 1061. Lexicographically Smallest Equivalent String
# ----------------------------------------------------------------------------------------
# You are given two strings of the same length s1 and s2 and a string baseStr.
# We say s1[i] and s2[i] are equivalent characters.
# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
# Constraints:
# 1 <= s1.length, s2.length, baseStr <= 1000
# s1.length == s2.length
# s1, s2, and baseStr consist of lowercase English letters.
# ----------------------------------------------------------------------------------------

def findLexicographicallySmallestEquivalentString(s1, s2, baseStr):
    parent = {chr(i): chr(i) for i in range(ord('a'), ord('z') + 1)}        # Initialize parent mapping for each character

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY

    for a, b in zip(s1, s2):
        union(a, b)

    result = []
    for ch in baseStr:
        result.append(find(ch))

    return ''.join(result)

if __name__ == "__main__":
    # Test cases
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    print(findLexicographicallySmallestEquivalentString(s1, s2, baseStr))  # Output: "makkek"

    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    print(findLexicographicallySmallestEquivalentString(s1, s2, baseStr))  # Output: "hdld"

# ------------------------------------------------------------------------
# Time Complexity: O(n + m), where n is the length of s1 (or s2) and m is the length of baseStr.
# Space Complexity: O(1) (since the parent mapping is fixed for 26 lowercase letters)
# Pattern: Union-Find (Disjoint Set Union)
# ------------------------------------------------------------------------