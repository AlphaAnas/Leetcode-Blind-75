# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

"""
You should aim for a solution with O(n) time and O(n) space, where n is the size of the input array.

"""


# //////////////// UNOPTIMIZED APPROACH - O(n^2) time and O(n) space ////////////////
'''
def sorter( d):
        nums = list(d.keys())
        for i in range(len(nums)-1):
                for j in range(len(nums) - i - 1):
                        if d[nums[j]] < d[nums[j+1]]:
                                nums[j], nums[j+1] = nums[j+1] , nums[j]
        return nums
                
def topKFrequent(nums, k):
    
        d = {}
        for ele in nums:
                d[ele] = d.get(ele, 0) + 1
        
        sorted_list_r = []
        sorted_list_r = sorter(d)
        final = []
        final = sorted_list_r[:k]
        return final

'''


# //////////////////// LINEAR TIME APPROACH ///////////////////////
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
        




print(topKFrequent([1,1,1,2,2,3],2 )) # output [1,2]
# print(topKFrequent([1,2,2,3,3,3],2 )) # output [2,3]
# print(topKFrequent([7,7], 1)) # output [7]
