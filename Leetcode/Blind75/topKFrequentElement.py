# 347. Top K Frequent Elements
# Medium
# Topics
# premium lock icon
# Companies
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



def topKFrequent(nums, k):

    d ={}
    for n in nums:
        d[n] = d.get(n, 0) + 1
    counts = [[] for i in range(len(nums) + 1)]

    for n,c in d.items():
        counts[c].append(n)    
    f = []
    for i in range(len(counts) - 1, 0, -1):
        for n in counts[i]:
            f.append(n)
            if len(f) == k:
                return f

print(topKFrequent([1,1,1,2,2,3],2 )) # output [1,2]
print(topKFrequent([1,2,2,3,3,3],2 )) # output [2,3]
print(topKFrequent([7,7], 1)) # output [7]
        