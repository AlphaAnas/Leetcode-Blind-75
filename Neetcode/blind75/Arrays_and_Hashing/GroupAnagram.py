# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.




def groupAnagrams(strs):
    hashmap = {}
    for words in strs:
        d = {}
        for c in words:
            d[c] = d.get(c, 0) + 1

        key = tuple(sorted(d.items()))
        # print(key)
        if key in hashmap:
            hashmap[key].append(words)
        else:
            hashmap[key] = [words]

    # print(list(hashmap.values()))
    return list(hashmap.values())


print(groupAnagrams(["act","pots","tops","cat","stop","hat"])) # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(groupAnagrams(strs = ["x"])) # Output: [["x"]]
