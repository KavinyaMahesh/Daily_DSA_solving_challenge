def two_sum(arr, target):

    '''
    We will select the element of the array one by one using a loop (say i).
    Then we will check if the other required element (i.e. target - arr[i]) exists in the HashMap.
    If that element exists, then we will return "YES" for the first variant or we will return the current index i.e. i, and the index of the element found using map i.e. mp[target - arr[i]].
    If that element does not exist, then we will just store the current element in the HashMap along with its index. Because in the future, the current element might be a part of our answer.
    Finally, if we are out of the loop, that means there is no such pair whose sum is equal to the target. In this case, we will return either "NO" or {-1, -1} as per the variant of the question.
    '''
    
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
