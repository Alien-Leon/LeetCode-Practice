class Solution:
    # 绝对众数(出现次数 > n/2)
    # Hash统计 O(n) 空间O(n)
    # 直接排序返回中间数，O(nlgn)
    """
    摩尔投票法 时间O(n) 空间O(1)
    设定候选者为第一元素，初始票数为1，随后扫描并统计票数
    非候选者的投票则将票数减一，当票为0时更换候选者

    """

    def majorityElement(self, nums) -> int:
        count = 1
        m = nums[0]
        for i in nums[1:]:
            if i == m:
                count += 1
            else:
                count -= 1
            if count == 0:
                count = 1
                m = i
        # print(m)
        return m


s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))