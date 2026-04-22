# oYu are given an integer array nums and an integer k. Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:

# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions. If no subarray meets the conditions, return 0.

# A subarray is a contiguous non-empty sequence of elements within an array.

def maximumSubarraySum(nums, k):

    d = {}
    j = 0
    maxSum, currSum = 0, 0
    for i in range(len(nums)):
        currSum += nums[i]
        d[nums[i]] = d.get(nums[i], 0) + 1
        if (i >= k - 1 ):
            if len(d.keys()) == k:
                maxSum = max(maxSum, currSum)
            currSum -= nums[i - k + 1]
            #  decrease the value
            d[nums[i - k + 1]] -= 1
            #  if the value is 0, remove the key
            if d[nums[i - k + 1]] == 0:
                del d[nums[i - k + 1]]
    return maxSum



# Example 1:

# Input: nums = [1,5,4,2,9,9,9], k = 3
print(maximumSubarraySum([1,5,4,2,9,9,9], 3))
# Output: 15



# Input: nums = [4,4,4], k = 3
print(maximumSubarraySum([4,4,4], 3))
# Output: 0

