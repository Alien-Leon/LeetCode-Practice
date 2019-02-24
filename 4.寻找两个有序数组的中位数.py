# 题解参见https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/

# 引申搜索两个有序数组的第k大数

class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        # 计算中位数只需找到数组最中间的两个数（偶数长度） 或 最中间的一个数（奇数长度）
    
        len1, len2 = len(nums1), len(nums2)
        length = len1 + len2
        if len1 > len2:
            len1, len2, nums1, nums2 = len2, len1, nums2, nums1
        
        mini, maxi, half = 0, len1, int((len1+len2+1) / 2)

        while 1:
            i = int((mini + maxi) / 2)
            j = half - i
            # print(mini, '---', maxi)
            # print(nums1[:i],':',nums1[i:])
            # print(nums2[:j],':',nums2[j:])

            if i > 0 and nums1[i-1] > nums2[j]:
                maxi -= 1 
            elif i < len1 and nums2[j-1] > nums1[i]:
                mini += 1
            else:     
                if i == 0:
                    left_max = nums2[j-1]
                elif j == 0:
                    left_max = nums1[i-1]
                else:
                    left_max = max(nums1[i-1], nums2[j-1])
                    
                if length % 2 == 0:
                    if i == len1:
                        right_min = nums2[j]
                    elif j == len2:
                        right_min = nums1[i]
                    else:
                        right_min = min(nums1[i], nums2[j])
                    return (left_max + right_min) / 2
                else:
                    return left_max
            

s = Solution()
nums1 = []
nums2 = [2]
# nums1 = [1,5,7]
# nums2 = [2,4,6,8]
# [1,1,2,4,6,7,8]
s.findMedianSortedArrays(nums1, nums2)

