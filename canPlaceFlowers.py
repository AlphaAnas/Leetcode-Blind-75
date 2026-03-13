"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""


def canPlaceFlowers(flowerbed, n):

    count = 0
    for i in range(len(flowerbed)):

        if flowerbed[i] == 0:

            empty_l =  i == 0 or (flowerbed[i-1] == 0)
            empty_r = i == len(flowerbed) - 1 or (flowerbed[i+1] == 0 )
            if empty_l and empty_r:
                flowerbed[i] = 1
                count += 1

    return count >= n

    # previous failing solution
    # if len(flowerbed) == 0: return False
    # elif len(flowerbed) == 1: 
        
    #     return ((flowerbed[0] == 0 and n ==  1) or (flowerbed[0] == 1 and n ==  0))
    

    

    # last = -1
    # if len(flowerbed) % 2 != 0:
    #     last = flowerbed[-1]
    #     # print("flowerbed, before", flowerbed)
    #     flowerbed = flowerbed[:-1]
    #     # print("flowerbed, after", flowerbed)
    # l = []
    # # considering flowerbed is of even lenght now
    # for i in range(0, len(flowerbed) - 1, 2):
    #     if n == 0: return True

    #     c = flowerbed[i]
    #     b = flowerbed[i+1]

    #     if c == b == 0:
           
    #         n-=1
    #         l.append(True)
    #     else:l.append(False)
    # print(l)
    # print(last)
    # if l[-1] == True and last ==0:
    #     print(n)
    #     n-=1
    # elif flowerbed[-1] ==0 and last ==0 and l[-1]:
    #     n-=1

    # return n == 0 
            
    
    

    




print(canPlaceFlowers([1,0,0,0,1], 1))  # true
print(canPlaceFlowers([1,0,0,0,1], 2 )) # false
print(canPlaceFlowers([1,0,0,0,1,1], 2 )) # false
print(canPlaceFlowers([0,0,0,0,0,0,0], 2 )) # true
print(canPlaceFlowers([0,0,1,0,1,0,0], 2 )) # true
print(canPlaceFlowers([1,0,0,0,1,0,0], 2 )) # true
print(canPlaceFlowers([1], 0 )) # true
