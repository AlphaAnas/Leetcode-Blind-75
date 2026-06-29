

# variable sized sliding window problem
def findSubArraySum(a, t):
    currentSum = 0
    l, r = 0, 1
    while r < len(a) :
        currentSum = sum(a[l:r])
        if currentSum > t:
            l +=1 
        elif currentSum < t:
            r += 1 
        else:
            return a[l:r]
    return []


    # ///////////////////// O(2n)  ////////////////////
    start = 0
    currentSum = a[0]
    for end in range(len(a)):
        currentSum += a[end]
        while currentSum > t:
            start += 1
            currentSum -= a[start]
        if currentSum == t:
            return a[start:end]
    return []




print(findSubArraySum([3,1,4,9,2,1,7,5], 10)) # output [2,1,7]