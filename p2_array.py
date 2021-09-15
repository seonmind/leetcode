class Solution:
    def maxProfit(self, prices):
        profit=0
        for i in range(len(prices)-1):
            if prices[i]<prices[i+1]:
                profit+=(prices[i+1]-prices[i])
        return profit
prices=[7,1,5,3,6,4]
sol=Solution()
print(sol.maxProfit(prices))
