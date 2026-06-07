class Solution:
    def longestConsecutive(self, nums):
        n=len(nums)
        if n==0:
            return 0
        nums.sort()

        last_smallest=float('-inf')
        cnt=0
        longest=1
        

        for i in range(n):
            if nums[i] - 1 ==last_smallest:
                cnt+=1
                last_smallest=nums[i]
                
            elif nums[i]!= last_smallest:
                cnt=1
                last_smallest=nums[i]

            longest=max(cnt, longest) 

        return longest              

if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    sol = Solution()
    result = sol.longestConsecutive(nums)
    print("Length of the longest consecutive elements sequence is:", result)        