
# 647. Palindromic Substrings
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.




def countSubstrings(s):

 

  
        out = 0
        for i in range(len(s)):
                for j in range(i, len(s)):
                        if s[i:j+1] == s[i:j+1][::-1]:
                               out += 1

        return out        
            





print(countSubstrings("abc"))  # Output: 3
    
print(countSubstrings("aaa"))  # Output: 6

print(countSubstrings("ababa"))  # Output: 9