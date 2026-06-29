


def lengthOfLongestSubstring(s):

    # longest = 0
    # start = 0
    # substring = {}
    # for i in range(1, len(s)):
    #     substr = s[start : i + 1]
    #     for _ in substr:
    #         substring[_] = substring.get(_, 0) + 1
    #         if substring.get(_,0) > 1:
    #             start += 1
    #             substring[_] -= 1
    #     longest = max(longest, len(list(substring.keys())))
    # return longest   

    # ////////////////////// Sliding window approach //////////////// 
    start = 0
    substring = []
    d = {}
    maxlen = 0
    for end in range(len(s)):
        substring = s[start:end + 1]
        CharAreUnique = True if len(substring) == len(set(substring)) else False
        if CharAreUnique:
            if len(substring) > maxlen:
                maxlen = len(substring)
        elif not(CharAreUnique):
            start += 1
    
    return maxlen






        


print(lengthOfLongestSubstring(s="pwwkew")) # output 3
print(lengthOfLongestSubstring("au")) # output 2
print(lengthOfLongestSubstring("zxyzxyz")) # output 3
print(lengthOfLongestSubstring("xxxx")) # output 1


