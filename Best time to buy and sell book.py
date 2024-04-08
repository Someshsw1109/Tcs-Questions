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
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

'''
'''There are two solution for this question'''
# Solution-1:- 
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        Minimum_price = prices[0]
        Maximum_profit = 0
        
        #we can use both "for" and "while" loop to solve this question.
        for i in prices[1:]:
            Minimum_price = min(Minimum_price, i)
            Maximum_profit = max(Maximum_profit, i - Minimum_price)
        return Maximum_profit

# Solution-2:- 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices or len(prices) < 2:
            return 0
        
        Minimum_price = prices[0]
        Maximum_profit = 0
        i = 1
        
        # Using While loop
        while i < len(prices):
            Minimum_price = min(Minimum_price, prices[i])
            Maximum_profit = max(Maximum_profit, prices[i] - Minimum_price)
            i += 1
        return Maximum_profit

# The number of occurence:- 2