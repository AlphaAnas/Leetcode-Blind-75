# # You are given an integer array heights where heights[i] represents the height of the 
# the ith bar
# # You may choose any two bars to form a container. Return the maximum amount of water a container can store.



def maxArea(heights):

    # /////////////// O(N**2) //////////////////
    # final = 0
    # for i in range(len(heights)):
    #     for j in range(i + 1, len(heights)):
    #         width = j - i
    #         height = min(heights[i], heights[j])
    #         final = max(final, width * height)
    # return final
    # ////////////////// O(N) ////////////////////
    final = 0
    l = 0
    r = len(heights) -1
    while l < r:
        
        final = max(final, (r - l) * min(heights[l], heights[r]))

        
        if heights[l] < heights[r]:
            l += 1
        elif heights[l] >= heights[r]:
            r -= 1
    return final




print(maxArea([1,7,2,5,4,7,3,6])) # output 36
print(maxArea([2,2,2])) # output  4