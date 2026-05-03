
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.





def hasDuplicate(nums):

        hashmap = {}
        for i in range(len(nums)):
                hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
                if hashmap[nums[i]] > 1:
                        return True
        return False



print(hasDuplicate([1, 2, 3, 3])) # true
print(hasDuplicate([1, 2, 3, 4])) # false