def two_sum(arr, target):
    mp={}

    for i , num in enumerate(arr):
        complement=target-num
        if complement in mp:
            return mp[complement], i
        
        mp[num]=i

    return [-1,-1]

if __name__=="__main__":
    arr=[2,7,11,15]
    target=9
    result=two_sum(arr, target)
    print(f"Indices of the two numbers that add up to {target} are: {result}")
