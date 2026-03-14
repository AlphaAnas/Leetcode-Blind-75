"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

"""
import math


def productExceptSelf(nums):

    # // O(n) solution
    ans = [1] * len(nums)
    p, s= 1, 1
    for i in range( len(nums)):
        ans[i] *= p
        p *= nums[i] 
    for i in range(len(nums)-1, -1, -1):
        ans[i] *= s
        s *= nums[i] 
    return ans

    # // O(n^2) so doesn't work
    # l, r = 0, len(nums) -1
    # suffix = []
    # prefix = []
    # for i in range(len(nums)):
    #     r = math.prod(nums[i+1:])
    #     suffix.append(r)
    #     l = math.prod(nums[:i])
    #     prefix.append(l)
    
    # return [p * s for p,s in zip(prefix, suffix)]





# print(productExceptSelf([1,2,3,4])) #Output: [24,12,8,6]

# prefix = [1, 1, 2, 6]
# suffix = [24, 12, 4, 1]
# answer = prefix . suffix 

print(productExceptSelf( [-1,1,0,-3,3])) # Output: [0,0,9,0,0]
 
