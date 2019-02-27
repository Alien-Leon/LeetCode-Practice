"""
线性时间复杂度且不使用额外空间
1.恒定律：A ^ 0 = A
2.归零率：A ^ A = 0
3.交换律：A ^ B = B ^ A
4.结合律：(A ^ B) ^ C = A ^ (B ^ C)
异或可以做的事情：
异或可以快速比较两个值是否相等 a ^ b == 0，效率非常高，比 a - b == 0 高很多。
异或还能在不定义临时变量的情况下，交换两个值（经典题目）
a = a ^ b
b = a ^ b  // a ^ b ^ b = a ^ 0 = a
a = a ^ b  // a ^ b ^ a = b ^ 0 = b


那么对于下式
a ^ b ^ c ^ b ^ c ^ d ^ a
= a ^ a ^ b ^ b ^ c ^ c ^ d
= 0 ^ 0 ^ 0 ^ d
= d

"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res ^= i
        return res