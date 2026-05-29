


def hasSubStringAnagram(s,anagram):

    a = set(anagram)
    k = len(a)

    for i in range(len(s) - k):
        sub_str = s[i : i+k]
        if a == set(sub_str):
            return True
    return False


print(hasSubStringAnagram("greyhounds", "hoy" )) # output : True 
