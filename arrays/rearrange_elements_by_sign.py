def rearrange(nums):
    n=len(nums)
    ans=[0]*n

    pos_index=0
    neg_index=1

    for i in range(n):
        if nums[i]>=0:
            ans[pos_index]=nums[i]
            pos_index+=2
        else:
            ans[neg_index]=nums[i]
            neg_index+=2
    return ans

if __name__ == "__main__":
    arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
    result = rearrange(arr)
    print("Rearranged array:", result)