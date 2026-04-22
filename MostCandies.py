
def kidsWithCandies( candies: list[int], extraCandies: int) -> list[bool]:

     output: list[bool] = []
     highest = max(candies)
     for ele in candies:
        if int(ele) + extraCandies >= highest:
            output.append(True)
        else:
            output.append(False)
        


     return output

        


print(kidsWithCandies([2,3,5,1,3], 3))
print(kidsWithCandies([4,2,1,1,2], 1))
print(kidsWithCandies([12,1,12], 10))
