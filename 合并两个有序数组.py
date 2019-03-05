class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        从数组末尾开始归并填充
        """
        i = m - 1
        j = n - 1
        k = len(nums1) - 1
        while i > -1 and j > -1:    
            if nums1[i] >= nums2[j]:        
                nums1[k] = nums1[i]
                i -= 1
            else:      
                nums1[k] =  nums2[j]
                j -= 1
            k -= 1

        while i > -1:
            nums1[k] = nums1[i]
            i -= 1
            k -= 1
        while j > -1:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
        print(nums1)
        

s = Solution()
# s.merge([1,2,3,0,0,0], 3,[2,5,6],3)
s.merge([0], 0,[2],1)