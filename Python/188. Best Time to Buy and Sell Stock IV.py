'''
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.
Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        res = 0
        n = len(prices)
        if n < 2:
            return 0
        if k > n//2:
            for i in range(1,n):
                if prices[i]>prices[i-1]:
                    res += prices[i]- prices[i-1]
            return res
        
        sell = [0]*(k+1)
        buy = [-float("inf")]*(k+1)
        
        for i in range(len(prices)):
            for j in range(1, k+1):
                buy[j] = max(buy[j], sell[j-1]-prices[i])
                sell[j] = max(sell[j], buy[j]+prices[i]) # !!WatchOut: it's buy[j] not buy[j-1]
        return sell[k]
