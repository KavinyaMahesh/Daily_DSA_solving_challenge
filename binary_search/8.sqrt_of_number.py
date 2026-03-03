def sqrt(x):
    if x<2:
        return x
    left,right=0,x//2

    ans=-1

    while left<=right:
        mid=(left+right)//2
        if mid*mid<=x:
            left=mid+1
            ans=mid
        else:
            right=mid-1
    return ans

# Test cases
print(sqrt(16))  # Output: 4
print(sqrt(8))   # Output: 2

