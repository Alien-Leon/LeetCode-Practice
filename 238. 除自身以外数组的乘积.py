class Solution:
    """要求：请不要使用除法，且在 O(n) 时间复杂度内完成此题"""
    def productExceptSelf(self, nums):
        prod = [1 for i in range(len(nums))]
        p = 1
        for i in range(len(nums) - 1):
            p *= nums[i]
            prod[i+1] *= p
        p = 1
        for j in range(len(nums) - 1, 0, -1):
            p *= nums[j]
            prod[j-1] *= p
        # print(prod)
        return prod

s = Solution()
s.productExceptSelf([1,2,3,4])
        