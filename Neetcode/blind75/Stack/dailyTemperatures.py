'''
Daily Temperatures
Medium
Topics
Company Tags
Hints
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

'''
from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    ## =============== BRUTE FORCE SOLUTION =========================
    # result = []
    # for i in range(len(temperatures)):
    #     counter = 0
    #     for j in range(i + 1, len(temperatures)):
    #         counter += 1
    #         if temperatures[i] < temperatures[j]:
    #             result.append(counter)
    #             break
    #     else:
    #         result.append(0) # j loop ended and we didn't find any bigger value

    # return result
    # ==================================================================

    ## ====================== O(n) optimized solution =====================

    temp = temperatures
    stk = []
    result = [0] * len(temp)
    for i, val in enumerate(temp):

        while (stk and stk[-1][0] < val): # this is not O(n^2) but this is O(n+n) since we are just adding n things and removing n things
            temp_pop, ind = stk.pop()
            result[ind] = i - ind

        stk.append((val,i))
    return result
    # =======================================================================


            


temperatures = [30,38,30,36,35,40,28] # Output: [1,4,1,2,1,0,0]

print(dailyTemperatures(temperatures))
temperatures = [22,21,20] # Output: [0,0,0]
print(dailyTemperatures(temperatures))