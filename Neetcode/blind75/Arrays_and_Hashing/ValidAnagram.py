# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.




def isAnagram(s, t):
    h1 = {}
    h2 = {}

    if len(s) != len(t):
        return False
    

    for i in s:
        h1[i] = h1.get(i, 0) + 1
    
    for i in t:
        h2[i] = h2.get(i, 0) + 1

    for k, v in h1.items():
        if h2.get(k, -1) != v:
            return False
        
    return True

    
    


print(isAnagram( s = "racecar", t = "carrace"))
print(isAnagram( s = "jar", t = "jam"))

