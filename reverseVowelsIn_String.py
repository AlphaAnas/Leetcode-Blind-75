"""
345. Reverse Vowels of a String
Easy
Topics
premium lock icon
Companies
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Leetcode - medium
"""
 

def reverseVowels(s):

    s = list(s)
    vowels = ['a', 'e', 'i','o', 'u']
    v = []

    for i in range(len(s)-1, -1, -1):
        if s[i].lower() in vowels: v.append(s[i])

    count = 0
    for i in range(len(s)):
        if s[i].lower() in vowels:
            s[i] = v[count]
            count += 1
    return "".join(s) 




print(reverseVowels("IceCreAm"))    #Output= "AceCreIm"
print(reverseVowels("leetcode")) #Output: "leotcede"