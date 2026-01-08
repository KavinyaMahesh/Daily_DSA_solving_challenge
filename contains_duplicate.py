def contains_duplicate(arr):
    ans=0
    for num in arr:
        ans^=num
    return ans

if __name__=="__main__":
    arr=[1,2,3,1]
    result=contains_duplicate(arr)
    print(f"The element that appears only once in the array is: {result}")