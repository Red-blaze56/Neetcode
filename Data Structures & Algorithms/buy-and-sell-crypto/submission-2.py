class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        MAXPROF,profit = 0,0
        while l<r and r<len(prices):
            profit = prices[r] - prices[l]
            if prices[l] < prices[r]:
                MAXPROF = max(MAXPROF, profit)
            else:
                l=r
            r+=1
        return max(MAXPROF, profit)
        