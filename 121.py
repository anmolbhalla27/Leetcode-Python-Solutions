prices = [7,1,5,3,6,4]
minn = 99999
profit = 0
for i in range(0,len(prices)):
    if(prices[i]<minn):
        minn = prices[i]
    else:
        if((prices[i]-minn)>profit):
            profit = (prices[i]-minn)
print(profit)