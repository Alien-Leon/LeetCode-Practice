"""
若直接计算A+B+C+D的和则会带来O(n^4)的过高复杂度
因此考虑将四个数组分成两两先计算，采用字典存储两个数组的和，换来高效率。
"""
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        d = {}
        count = 0
        for i in A:
            for j in B:
                d[i+j] = d.get(i+j, 0) + 1

        for i in C:
            for j in D:
                if -i-j in d:
                    count += d[-i-j]
        return count
        