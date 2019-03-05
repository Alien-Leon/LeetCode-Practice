from functools import cmp_to_key

"""
给定一组非负整数，重新排列它们的顺序使之组成一个最大的整数。

示例 1:

输入: [10,2]
输出: 210
示例 2:

输入: [3,30,34,5,9]
输出: 9534330

思路：将数字转为字符串后自定义排序比较 x+y, y+x, 
"""
class Solution:
    def largestNumber(self, nums: list) -> str:
        # def count_length(x):
        #     count = 1
        #     x = int(x/10)
        #     while x:
        #         count *= 10
        #         x = int(x/10)
        #     return count

        # count = {}
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        # print(nums)
        def rule(x, y):
            # print('cmp', x, y)
            xy, yx = x+y, y+x 
            for i, j in zip(xy, yx):
                # print('cmp',i,j)
                if i < j:
                    return -1
                elif i > j:
                    return 1
            return 0

        # list.sort()
        nums.sort(key=cmp_to_key(rule), reverse=True)
        
        # print(nums)
        i = 0
        s = ''.join(nums)
        # 去除前导0， 如'00'
        while i < len(s):
            if s[i] == '0':
                i += 1
            else:
                break
        if i > 1:
            return s[i-1:]
        return s

s = Solution()
s.largestNumber([3,30,34,5,9])
s.largestNumber([128, 12])
s.largestNumber([1,1,1])
print(s.largestNumber([0,0]))