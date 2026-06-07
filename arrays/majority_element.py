def maj_element(nums):
    cnt=0
    el=None

    for num in nums:
        if cnt==0:
            cnt=1
            el=num
        elif num==el:
            cnt+=1
        else:
            cnt-=1

    return el
if __name__=="__main__":
    result = maj_element([3,2,3])
    print("Majority element is:", result)              