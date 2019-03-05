# 困难，未完成！
# TODO
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        ar = [[0 for i in range(N+1)] for j in range(K+1)]

        for j in range(1, N+1):
            ar[1][j] = j

        for i in range(2, K+1):
            for j in range(1, N+1):
                minimum = float('inf')

                for k in range(1, j+1):
                    minimum = min(minimum, max(ar[i][j-k], ar[i-1][k-1]))
                ar[i][j] = minimum + 1
        # for i in ar:
        #     print(i)

        # print(ar[K][N])
        return ar[K][N]

s = Solution()
s.superEggDrop(2, 6)