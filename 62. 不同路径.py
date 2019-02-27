from math import factorial
class Solution(object):
    # 使用组合逻辑速度最快，也可使用动态规划但时间复杂度为O(n*m)
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        def combination(a, b):
            return factorial(a) / (factorial(a-b) * factorial(b))
        return int(combination(n+m-2, m-1))

s = Solution()
print(s.uniquePaths(7,3))