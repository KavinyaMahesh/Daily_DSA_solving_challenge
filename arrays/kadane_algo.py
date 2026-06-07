def max_subarray_sum(arr):
    if not arr:
        return 0
    
    current_sum = max_so_far = arr[0]
    
    for x in arr[1:]:
        # Decide: add to current subarray or start a new one
        current_sum = max(x, current_sum + x)
        # Update the overall global maximum
        max_so_far = max(max_so_far, current_sum)
        
    return max_so_far

if __name__=="__main__":

    result = max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print("Maximum subarray sum is:", result)