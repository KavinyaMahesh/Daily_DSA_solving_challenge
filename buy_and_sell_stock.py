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