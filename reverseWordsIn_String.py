"""

Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

""" 

def reverseWords(s):

    s = s.strip(" ").split(" ")
    
    r = [word for word in reversed(s) if word.isalnum()]

    return " ".join(r)


print(reverseWords("the sky is blue")) # "blue is sky the"
print(reverseWords("  hello world  ")) # Output: "world hello"
print(reverseWords("a good   example")) # Output: "example good a"
print(reverseWords("EPY2giL")) # Output: "EPY2giL"
 