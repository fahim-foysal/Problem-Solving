from traceback import print_exc


def maxProfit(prices):
        profit=0
        sub=0
        x=min(prices)
        print(x)
       
        y=max(prices)
        print(y)
        if prices.index(y, 0, len(prices))> prices.index(x, 0, len(prices)):
            profit=y-x

        return profit
ls=[7,1,5,3,6,4]

print(maxProfit(ls))