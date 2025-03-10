#00121번 Best Time to Buy and Sell Stock
'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
'''
# 198 / 212 testcases passed
# FIXME: Time Limit Exceeded
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         profit = 0
#         for i in range(len(prices)):
#             for j in range(i+1,len(prices)):
#                 if profit< (prices[j] - prices[i]):
#                     profit = prices[j] - prices[i]
#         return profit

# 198 / 212 testcases passed
# FIXME: Time Limit Exceeded
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         length = len(prices)
#         profit = 0
#         tempList = sorted(prices)
#         maxProfit = tempList[length-1] -tempList[0] 
#         for i in range(length):
#             for j in range(i+1,length):
#                 if profit< (prices[j] - prices[i]):
#                     profit = prices[j] - prices[i]
#                 if profit == maxProfit:
#                     return maxProfit
#         return profit

# 178 / 212 testcases passed 
# FIXME: Wrong Answer 
# class Solution(object):
#     def maxProfit(self, prices):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         a = prices[0]
#         for i in range(len(prices)-1):
#             if a>prices[i]:
#                 a = prices[i]

#         b = a
#         for i in range(prices.index(a), len(prices)):
#             if b< prices[i]:
#                 b = prices[i]
#         return b-a

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]
        profit = 0
        for price in prices:
            if minPrice > price:
                minPrice = price
            else:
                profit = max(profit, price - minPrice)

        return profit
