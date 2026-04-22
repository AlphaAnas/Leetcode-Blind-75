


def printFirstNegative(nums, k):

    negatives = []
    i = 0
    j = 0
    for i in range(len(nums)):
        if nums[i] < 0:
            negatives.append(nums[i])
        if (i - j + 1) == k:
            
            if len(negatives) > 0:
                print(negatives[0], end=" ")
             
            else:
                print(0, end=" ")
            
            if negatives and negatives[0] == nums[j]:
                negatives.pop(0)
        
            j += 1

printFirstNegative([1, -2, -3, 5, -1, 2], 3) # output : -2, -3, -1
