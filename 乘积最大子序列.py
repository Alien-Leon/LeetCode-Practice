# https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/05.01.md
class Solution:
    def maxProduct(self, nums) -> int:
        maxend = nums[0]
        minend = nums[0]
        maxmum = maxend
        for i in range(1, len(nums)):
            e1, e2 = maxend, minend
            maxend = max(e1 * nums[i], e2 * nums[i], nums[i])
            minend = min(e1 * nums[i], e2 * nums[i], nums[i])
            # print(maxend, minend)
            maxmum = max(maxmum, maxend)

        print(maxmum)
        return maxmum


s = Solution()
s.maxProduct([-4,-3,-2])
                    