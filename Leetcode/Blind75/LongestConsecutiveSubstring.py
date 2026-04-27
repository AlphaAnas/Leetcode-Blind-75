# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.


import string

from pyparsing import nums

def longestConsecutive(nums):
        


        # ////////////// NAIVE SOLUTION (O(n log n)) //////////////
        nums = sorted(set(nums))
        print("sorted: ", nums)
        if not nums:            return 0    
        s = str(nums[0])
        array =  []
        for i in (nums)[1:]:
            print("i: ", i)
            print("s: ", s[-1])
            if int(s[-1]) + 1 == i:
                s += str(i)
                print("string: ", s)
            else:
                array.append(s)
                s = str(i)


        array.append(s)
        return max(len(seq) for seq in array)



print(longestConsecutive([1,0,-1])) # 3
# print(longestConsecutive([100,4,200,1,3,2])) # 4
# print(longestConsecutive([0,3,7,2,5,8,4,6,0,1])) # 9
# print(longestConsecutive([1,0,1,2]))  # 3
 