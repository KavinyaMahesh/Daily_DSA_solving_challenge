class Solution:
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1    
        return nums

    def rotate(self, nums, k, direction):
        n = len(nums)
        k = k % n
        if direction == 'left':
            k = n - k
        # Step 1: Reverse the entire array
        nums = self.reverse(nums, 0, n - 1)

        # Step 2: Reverse the first k elements
        nums = self.reverse(nums, 0, k - 1)

        # Step 3: Reverse the remaining n-k elements
        nums = self.reverse(nums, k, n - 1)

        return nums        


if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    direction = 'left' 
    result = solution.rotate(arr, k, direction)
    print(f"Array after rotating {direction} by {k} positions: {result}")        