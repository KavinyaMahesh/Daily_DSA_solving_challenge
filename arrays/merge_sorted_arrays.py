def merge(nums1, nums2, m , n):
    """
    Merges two sorted arrays nums1 and nums2 into a single sorted array in-place.
    
    Parameters:
    nums1 (List[int]): The first sorted array with a size of m + n, where the first m elements are valid.
    nums2 (List[int]): The second sorted array with n elements.
    m (int): The number of valid elements in nums1.
    n (int): The number of elements in nums2.
    
    Returns:
    None: The function modifies nums1 in-place to contain the merged sorted array.
    """
    # Start from the end of both arrays
    i = m - 1  # Pointer for the last valid element in nums1
    j = n - 1  # Pointer for the last element in nums2
    k = m + n - 1  # Pointer for the last position in nums1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    nums2 = [2, 5, 6]
    m = 3
    n = 3
    merge(nums1, nums2, m, n)
    print(nums1) 