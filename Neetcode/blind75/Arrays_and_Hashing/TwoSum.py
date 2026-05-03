
# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.



def twoSum(nums, target):


        hashmap = {}
        for i in range(len(nums)):
                req = target - nums[i]
                if req in hashmap:
                        
                        return [hashmap[req], i]
            
                hashmap[nums[i]] = i
        

        return []

print(twoSum(nums=[3,4,5,6], target = 7)) # [0, 1]
print(twoSum(nums = [4,5,6], target = 10)) # [0,2]
