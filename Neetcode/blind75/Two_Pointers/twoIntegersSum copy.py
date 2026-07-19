'''
Two Integer Sum II
Medium
Topics
Company Tags
Hints
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given target number target and index1 < index2. Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Your solution must use 
O
(
1
)
O(1) additional space.

'''


def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while (l < r):
        if (numbers[l] + numbers[r] == target):
            return [l + 1, r + 1]
        elif (numbers[l] + numbers[r] < target):
            l += 1
        elif (numbers[l] + numbers[r] > target):
            r -= 1
    return []


numbers = [1,2,3,4]
target = 3
print(twoSum(numbers, target)) # Output: [1,2]