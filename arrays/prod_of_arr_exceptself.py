class Solution:
    def productExceptSelf(nums):
        n = len(nums)
        ans = [1] * n

        prefix = 1
        for i in range(n):
            ans[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suffix
            suffix *= nums[i]

        return ans
    

if __name__ == "__main__":
    solution = Solution()
    result = solution.productExceptSelf([1, 2, 3, 4])
    print("Product except self:", result)



