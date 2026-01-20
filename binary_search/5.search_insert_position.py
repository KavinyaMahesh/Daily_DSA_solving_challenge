class Solution:
    def searchInsert(self,nums,target):
        low=0
        high=len(nums)-1
        ans=len(nums)
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>=target:
                ans=mid
                high=mid-1

            else:
                low=mid+1

        return ans            

        

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    target = 5
    solution = Solution()
    result = solution.searchInsert(nums, target)
    print(f"Insert position for target {target} is: {result}")        