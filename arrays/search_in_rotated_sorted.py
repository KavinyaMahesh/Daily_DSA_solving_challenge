def search_in_roated_sorted(arr,target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid=left+right//2

        if arr[mid]==target:
            return mid
        

        if arr[left]<=arr[mid]:
            if arr[left]<target<=arr[mid]:
                right=mid-1
            else:
                left=mid+1
        else:
            if arr [mid]<target<=arr[right]:
                left=mid+1
            else:
                right=mid-1 

    return -1


if __name__=="__main__":
    arr=[4,5,6,7,0,1,2]
    target=0
    result=search_in_roated_sorted(arr,target)
    print(f"Element {target} is found at index: {result}")


'''
Start by looking at the middle element of the array.
Check if this middle element is the target if yes, return its index immediately.
Now figure out which half of the array (left side or right side) is sorted.
If the left part is sorted:
Check if the target number falls within the range of that sorted part.
If it does, discard the right half and continue the search in the left part.
If it doesn’t, discard the left half and search in the right side.
If the right part is sorted:
Do the same check if the target is in that sorted part.
If yes, discard the left side and search in the right.
If not, discard the right and continue with the left.
Repeat this process of eliminating half the array until the target is found or the search space is empty.
'''    
