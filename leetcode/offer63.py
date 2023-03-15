class solution:
    def maxProfit(self,prices:'list[int]') -> int:
        cost,profit=float("+inf"),0
        for price in prices:
            cost=min(cost,price)
            profit=max(profit,price-cost)
        return profit