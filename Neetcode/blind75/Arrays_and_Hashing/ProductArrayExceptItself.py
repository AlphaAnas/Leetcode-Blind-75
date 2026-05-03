# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

# Each product is guaranteed to fit in a 32-bit integer.

# Follow-up: Could you solve it in 
# O
# (
# n
# )
# O(n) time without using the division operation?


def productExceptSelf(nums):

    suffix = [1] * len(nums) 
    for i in range(len(nums) -2, -1, - 1):

        suffix[i] =  suffix[i+1] * nums[i+1]

    prefix = [1] * len(nums) 
    for i in range(1, len(nums)):
        prefix[i] = prefix[i-1] * nums[i-1]


    for i in range(len(prefix)):
        return [i * j for i,j in zip(prefix, suffix)]



print(productExceptSelf([1,2,4,6])) # Output: [48,24,12,8]
# print(productExceptSelf([-1,0,1,2,3])) # Output: [0,-6,0,0,0]
# print(productExceptSelf())
