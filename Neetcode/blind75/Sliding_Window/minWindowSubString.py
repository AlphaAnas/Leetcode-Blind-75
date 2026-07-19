'''

Minimum Window Substring
Hard
Topics
Company Tags


Given two strings s and t, return the shortest substring of s such that every character in t, including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.

'''

def minWindow(s: str, t: str) -> str:
    charT, window = {}, {}
    for c in t:
        charT[c] = charT.get(c, 0) + 1
    res, resLen = [-1,-1] , float("infinity")
    l = 0
    have, need = 0, len(charT)
    for r in range(len(s)):
        curr = s[r]
        window[curr] = window.get(curr, 0) + 1
        if (curr in charT and window[curr] >= charT[curr]):
            have += 1
        
            while (have == need): # so we have all the character needed in list t
                winLen = r - l + 1
                if (winLen < resLen):
                    resLen = winLen
                    res = [l, r]
                # pop from left
                window[s[l]] -= 1
                if (s[l] in charT and window[s[l]] < charT[s[l]] ): # we have lost one element requried in list t
                    have -= 1
                l += 1


    l, r = res
    return s[l : r + 1] if resLen != float("infinity") else ""




s = "OUZODYXAZV"
t = "XYZ"


print(minWindow(s, t))  # Output: "YXAZ"


s = "xyz"
t = "xyz"

print(minWindow(s, t))  # Output: "xyz"


s = "x"
t = "xy"

print(minWindow(s, t)) # Output: ""