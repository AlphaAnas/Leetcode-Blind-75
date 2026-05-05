
# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).


def isPalindrome(s:str):

    if len(s) == 0:
        return False
    

    s_ = "".join([i.lower() for i in s if i.isalnum() ])
    # print(s_)

    l = 0
    r = len(s_) - 1
    print("l: ", l)
    print("r: ", r)
    while l < r and l != r:
        if s_[l] != s_[r]:
            return False
        r -= 1
        l += 1

    

    return True




print(isPalindrome(s=" ")) # output true
# print(isPalindrome("Was it a car or a cat I saw?")) # output true
# print(isPalindrome("tab a cat")) # output false 