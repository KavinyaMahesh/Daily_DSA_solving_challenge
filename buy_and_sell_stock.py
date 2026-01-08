def fun(arr):

    min_price=float('inf')
    max_profit=0    

    for price in arr:
        if price<min_price:
            min_price=price

        profit=price-min_price

        if profit>max_profit:
            max_profit=profit

    return max_profit

if __name__=="__main__":
    arr=[7,1,5,3,6,4]
    result=fun(arr)
    print(f"The maximum profit from the given stock prices is: {result}")

'''
Start iterating through the prices of the stock day-by-day.
Keep track of the minimum price seen so far.
At each day, calculate the profit if we sold today using the minimum price seen so far.
Check if this profit is better than the maximum profit seen so far.
Update the maximum profit if this is the new best.
Continue this process for all days and return the best profit found.
'''
