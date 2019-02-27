
class Solution:
    # 双指针的使用
    def threeSumClosest(self, nums, target):
        nums.sort()
        min_dif = 999999
        res = 0  
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                dif = abs(sum - target)
                if sum - target > 0:
                    k -= 1
                elif sum - target <= 0:
                    j += 1
                else:
                    return sum
                if dif < min_dif:
                    # print(sum, min_dif)
                    res = sum
                    min_dif = dif
        # print(res, min_dif)
        return res
                
s = Solution()
s.threeSumClosest([1,1,1,0], -100)