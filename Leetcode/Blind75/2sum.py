
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


def twoSum(nums , target, TYPE="ARRAY"):


    if TYPE == "ARRAY":
    #  //////////////// ARRAY BASED SOLUTION ///////////////////////////
    # //////// COMPLEXITY : O(n^2)  ///////////////////////////////////////////
            for i in range(len(nums)):
                if (target - nums[i]) in nums[i+1:]:
                    
                    ind = nums.index(target-nums[i], i+1)
                    
                    return [i, ind]
            return []

    elif TYPE == "HASHMAP":
            #  //////////////// HASHMAP BASED SOLUTION ///////////////////////////
            # //////// COMPLEXITY : O(n)  /////////////////////////////////////////
            d = {}
            for i in range(len(nums)):
                required = target - nums[i]
                if required in d:
                    return [i, d[required]]

                d[nums[i]] = i
            return []

    



print(twoSum([2,7,11,15],  9, "HASHMAP")) # Output: [0,1]

print(twoSum([3,2,4], 6, "HASHMAP") )# Output: [1,2]

print(twoSum([3,3], 6, "HASHMAP")) # Output: [0,1]

print(twoSum( [6, 6,6 ,6 ,6] , 5, "HASHMAP")) # output []

print(twoSum( [3, 3, 4 ,3, 3], 6, "HASHMAP")) # output [0,1]