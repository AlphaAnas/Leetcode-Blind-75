"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""


def canPlaceFlowers(flowerbed, n):


    if len(flowerbed) == 1:
        return flowerbed[0] == 0 and n == 1

    elif len(flowerbed) % 2 == 0:
        for i in range(0, len(flowerbed)-1, 2 ):
            if (flowerbed[i+1] == 0 and flowerbed[i] == 0):
                n -=1 
                if n == 0:
                    return True

        
    else:
        if (flowerbed[-1] == 0 and flowerbed[-2] == 0): 
            n -=1
            # print(n)
        flowerbed[:-1]
        # print(flowerbed)
        for i in range(0, len(flowerbed)-1, 2 ):
            if (flowerbed[i+1] == 0 and flowerbed[i] == 0):
                n -=1 
                if n == 0:
                    return True
        # print(n)

    return n == 0







# print(canPlaceFlowers([1,0,0,0,1],1)) # true
# print(canPlaceFlowers([1,0,0,0,1], 2)) # False
# print(canPlaceFlowers([1,0,0,0,1,0], 2)) # False
# print(canPlaceFlowers([1,0,0,0,0,1], 2)) # False
# print(canPlaceFlowers([1,0,0,0,0,0,1], 2)) # True
print(canPlaceFlowers([1,0,0,0,1,0,0] , 2)) # True
