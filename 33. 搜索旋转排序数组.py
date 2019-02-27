"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

为了lg n的复杂度，采用二分的搜索方法，每一次二分必定使得一部分为有序数组，另一部分为部分有序数组。
对有序数组采用二分查找，部分有序则继续二分递归直至有序。
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1

        def binary_search(ar, x, l, r):
            while l <= r:
                # print('binary', l, r)
                m = int((l + r) / 2)
                if ar[m] == x:
                    return m
                elif ar[m] < x:
                    l = m + 1
                else:
                    r = m - 1
            return -1

        def split_search(nums, target, left, right):
            if left == right:
                return left if nums[left] == target else -1
            x = -1
            if nums[left] <= nums[right]:
                x = binary_search(nums, target, left, right)
            else:
                mid = int((left + right) / 2)
                x = max(split_search(nums, target, left, mid), split_search(nums, target, mid + 1, right)) 
            return x
            
        x = split_search(nums, target, 0, len(nums)-1)
        print(x)
        return x
        


s = Solution()
s.search([4,5,6,7,0,1,2], 0)
