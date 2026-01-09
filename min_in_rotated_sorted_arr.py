def min_in_rotated(arr):
    left, right=0, len(arr)-1

    while left<right:
        mid=(left+right)//2

        if arr[mid]>arr[right]:
            left=mid+1
        else:
            right=mid

    return arr[left]


if __name__=="__main__":
    result = min_in_rotated([4,5,6,7,0,1,2])
    print("Minimum element in rotated sorted array is:", result)


'''
In a rotated sorted array, the smallest element represents the point of rotation. It is the only element that is smaller than its previous element. Since the array is sorted in two segments, we can use binary search to efficiently find this pivot point. By comparing the middle element with the rightmost element in the current search space, we can determine which half of the array contains the minimum element.
Initialize pointers to the start and end of the array.
While start is less than end, calculate the middle index.
If the middle element is greater than the rightmost element, move the start to mid + 1.
Else, move the end to mid (because mid can be the minimum).
When the loop ends, start will point to the minimum element.
'''    