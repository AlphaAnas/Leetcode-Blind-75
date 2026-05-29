


def maxSubArrayProduct(s, k):



# //////////////////// O(n) /////////////////

    current_prod = 1
    for i in range(k):
        current_prod *= s[i]
    max_prod = current_prod
    for i in range(len(s) - k):
        current_prod /= s[i]
        current_prod *= s[i+k]
        if current_prod > max_prod:
            max_prod = current_prod
    return max_prod


print(maxSubArrayProduct([1,4,1,6,-3,3,-5,2,26], 4)) # output 270
