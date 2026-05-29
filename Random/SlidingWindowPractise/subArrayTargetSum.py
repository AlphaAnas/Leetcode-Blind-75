


def subArrayTargetSum(s,k,t):

        count = 0
        current_sum = sum(s[0:k])
        if current_sum == t:
                count += 1
        for i in range(len(s) -k ):
                current_sum -= s[i]
                current_sum += s[i+k]
                if current_sum == t:
                        count += 1
        return count


print(subArrayTargetSum([2,3,2,2,3,1,3,8,5,0,2,4], 3, 7)) # output 5