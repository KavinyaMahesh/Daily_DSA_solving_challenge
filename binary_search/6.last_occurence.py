def last_occurence(arr, target):
    low, high=0, len(arr)-1
    ans=-1

    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            ans=mid
            low=mid+1

        elif arr[mid]>target:
            high=mid-1

        else:
            low=mid+1

    return ans

if __name__=="__main__":
    arr=[1,2,3,4,5,5,5,6,7]
    target=5
    print(last_occurence(arr,target))                