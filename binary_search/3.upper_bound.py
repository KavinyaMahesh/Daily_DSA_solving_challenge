def upper_bound(arr, target):
    left=0
    right=len(arr)

    ans=len(arr)

    while left<=right:
        mid=(left+right)//2

        if arr[mid]>target:
            ans=mid
            right=mid-1
        else:
            left=mid+1

    return ans

if __name__ == "__main__":
    arr = [1, 2, 4, 4, 5, 6, 8]
    target = 4
    index = upper_bound(arr, target)
    print(f"The upper bound index for {target} in {arr} is: {index}")

