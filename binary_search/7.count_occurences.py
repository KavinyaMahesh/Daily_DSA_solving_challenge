def first_occurence(arr, target):
    left, right=0 , len(arr)-1
    first=-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            first=mid
            right=mid-1
        elif arr[mid]>target:
            right=mid-1
        else:
            left=mid+1

    return first


def last_occurence(arr, target):
    left, right=0 , len(arr)-1
    last=-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            last=mid
            left=mid+1
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return last

def count_occurences(arr, target):
    first=first_occurence(arr, target)
    last=last_occurence(arr, target)

    if first==-1 or last==-1:
        return 0
    
    ans=last-first+1
    

    return ans


# Test cases
arr = [1, 2, 2, 3, 4, 4, 4, 5]
target = 4 
print(count_occurences(arr, target))  # Output: 3


        