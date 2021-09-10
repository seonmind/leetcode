def preflow(nums,n):
        for i in range(1,n+1):
            if nums[n-i] != nums[n]:
                if nums[n-i] < nums[n]:
                    return 1
                else:
                    return -1
def afterflow(nums,n):
    for i in range(n+1,len(nums)):
        if nums[i] != nums[n]:
            if nums[n] < nums[i]:
                return 1
            else:
                return -1
class Solution:
    def maxProfit(self, prices):
        sum=0
        priceflow=prices
        for i in range(len(prices)):
            if preflow(prices,i)*afterflow(prices,i)!=1:
                priceflow[i]==preflow(prices,i)
            else:
                priceflow[i]==0
        for i in range(len(prices)):
            if priceflow[i]==0:
                continue
            else:
                if priceflow[i]==1:
                    priceflow[i]=0
                    break
                else:
                    break
        for a in range(len(prices)):
            i=len(prices)-a-1
            if priceflow[i]==0:
                continue
            else:
                if priceflow[i]==-1:
                    priceflow[i]=0
                    break
                else:
                    break
        for i in range(len(prices)):
            sum+=priceflow[i]*prices[i]
        return sum
            
