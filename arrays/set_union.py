def find_union(nums1, nums2):

    Union=[]
    i,j=0,0
    n1,n2=len(nums1),len(nums2)
    while i<n1 and j<n2:
        if nums1[i]<nums2[j]:
            if not Union or Union[-1]!=nums1[i]:
                Union.append(nums1[i])
            i+=1
        elif nums1[i]>nums2[j]:
            if not Union or Union[-1]!=nums2[j]:
                Union.append(nums2[j])
            j+=1
        else:
            if not Union or Union[-1]!=nums1[i]:
                Union.append(nums1[i])
            i+=1
            j+=1

    while i<n1:
        if not Union or Union[-1]!=nums1[i]:
            Union.append(nums1[i])
        i+=1
    while j<n2:
        if  not Union or Union[-1]!=nums2[j]:
            Union.append(nums2[j])
        j+=1

    return Union


if __name__=="__main__":
    result = find_union([1,2,2,3,4],[2,3,5,6])
    print("Union of two sorted arrays is:", result)        
