# you are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

def maxProfit(prices: list[int]) -> int:

        # ///////////////// brute force ///////////////
        # current_profit = 0
        # for i in range(len(prices) - 1):
        #         for j in range(i+1, len(prices)):
        #                 val = prices[j] - prices[i]
        #                 current_profit = max(current_profit, val)
        # return current_profit

        # ///////////////////// Two pointer approach - O(n) /////////
        maxP = 0
        left = 0
        right = 1

        while right < len(prices):
                if prices[left] < prices[right]:
                        profit = prices[right ] - prices[left]
                        maxP = max(maxP, profit)
                else:
                        left = right
                right += 1
        return maxP


print(maxProfit(prices = [10,1,5,6,7,1])) # 6
print(maxProfit(prices = [10,8,7,5,2])) # 0 