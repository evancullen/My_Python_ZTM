# Given two strings s and t, return true if t is an anagram of s, and false otherwise. 

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. 
# Example 1: 
#  Input: s = "anagram", t = "nagaram" 
# Output: true 
# Constraints: 

# 1 <= s.length, t.length <= 5 * 10^4 
# s and t consist of lowercase English letters.

# Solution
def isAnagram(s, t):
    # Step 1: Check if the lengths of s and t are different.
    if len(s) != len(t):
        return False
    
    # Step 2: Create dictionaries to store character counts.
    s_count = {}
    t_count = {}
    
    # Step 3: Update character counts for s.
    for char in s:
        s_count[char] = s_count.get(char, 0) + 1
    
    # Update character counts for t.
    for char in t:
        t_count[char] = t_count.get(char, 0) + 1
    
    # Step 4: Compare the dictionaries.
    return s_count == t_count

# Example usage:
s = "pools"
t = "spool"
print(isAnagram(s, t))  # This will return True.
