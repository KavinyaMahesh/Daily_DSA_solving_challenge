def sortColors( nums):
    

    countz=0
    counto=0
    countt=0

    for num in nums:
        if num==0:
            countz+=1
        elif num==1:
            counto+=1
        else:
            countt+=1


    for i in range(countz):
        nums[i]=0
    for j in range(countz,countz+counto):
        nums[j]=1

    for k in range(countz+counto,countz+counto+countt):
        nums[k]=2  

    print(nums)

if __name__=="__main__":
    sortColors( [2,0,2,1,2,1,0])    
