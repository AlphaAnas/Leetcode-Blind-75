# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 
def threeSum(nums):


    # ////////////// O(n^2) //////// 
    d = {}
    for i, num in enumerate(nums):
        d[num] = i

    final = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if i != j:
                required = - (nums[i] + nums[j])
                if required in d and d[required] != i and d[required] != j:
                    final.add(tuple(sorted([nums[i], nums[j], required])))
                    

    return [list(t) for t in final]


print(threeSum( [-1,0,1,2,-1,-4])) # Output: [[-1,-1,2],[-1,0,1]]


print(threeSum([0,1,1])) # Output: []


print(threeSum([0,0,0])) # Output: [[0,0,0]]
