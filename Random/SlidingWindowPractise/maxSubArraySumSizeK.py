


def maxsubArray(s, k):

# //////////////////////// O(n*k) ////////////////
        # max_sum = 0
        # for i in range(len(s) -k + 1):
             
        #         current_sum = 0
        #         subset = s[i : i+k]
        #         for j in range(k):
        #                 current_sum += subset[j]
                
        #         max_sum = max(max_sum, current_sum)
        
        # return max_sum

# /////////////////////// O(n) ////////////////////////////

        current_sum = sum(s[:k])
        max_sum = current_sum
        for i in range(0, len(s) - k ):
              current_sum += s[i+k]  
              current_sum -= s[i]
              if current_sum > max_sum:
                     max_sum = current_sum
        return max_sum
                

                        



print(maxsubArray([1,4,1,10,25,3,5,0,26] , 4)) # output 43
