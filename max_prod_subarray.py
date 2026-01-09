def max_prod_subarray(arr):
    pre=1
    suf=1
    n=len(arr)
    maxx=float('-inf')
    ans=1

    for i in range(len(arr)):
        if pre==0:
            pre=1
        if suf==0:
            suf=1

        pre=pre*arr[i]

        suf=suf*arr[n-i-1]  

        ans=max(ans,pre,suf)

    return ans


if __name__=="__main__":
    result = max_prod_subarray([2,3,-2,4,-2,-30])
    print("Maximum product of array is:", result)

'''
Traverse the array from left to right (prefix) to build cumulative product.
Traverse the array from right to left (suffix) to catch subarrays ending at the back (helpful when max product is at the end or due to even negatives).
Reset the product to 1 whenever a zero is found, as it breaks the subarray continuity.
By comparing products in both directions at each step, we ensure we don’t miss any possible maximum.
'''    