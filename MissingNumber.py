
"""
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

 
"""
def missingNumber(nums):

    s = sorted(nums)
    for i in range(len(s)):
        if i != s[i]:
            return i
        
    return s[-1] + 1
            


print(missingNumber([3,0,1])) # output 2
print(missingNumber([0,1])) # output 2
print(missingNumber([9,6,4,2,3,5,7,0,1])) # output 8
