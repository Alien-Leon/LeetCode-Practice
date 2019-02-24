class Solution:
    def longestPalindrome(self, s: 'str') -> 'str':

        r = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        left = 0
        right = 1
        # 需要特别注意循环顺序， 由于需要访问r[i+1][j-1], 因此i的值需要先计算，故置于内层循环
        for j in range(0, len(s)):
            for i in range(0, j+1):
                if i == j:
                    r[i][j] = 1
                elif i == j + 1 or j == i + 1:
                    if s[i] == s[j]:
                        r[i][j] = 1
                        if right - left < j - i + 1:
                            right = j+1
                            left = i
                    else:
                        r[i][j] = 0
                else:
                    if s[i] == s[j]:
                        r[i][j] = r[i+1][j-1]
                        if r[i][j] and right - left < j - i + 1:
                            right = j+1
                            left = i

        # for i in r:
        #     print(i)
        # print(left, right)
        print(s[left:right])
        return s[left:right]

s = Solution()
s.longestPalindrome("abcda")
        