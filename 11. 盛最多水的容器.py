class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        双指针简单完成
        """
        left = 0
        right = len(height) - 1
        max_s = 0
        while left < right:
            dx = right - left
            if height[left] < height[right]:
                max_s = max(max_s, dx * height[left])
                left += 1    
            else:
                max_s = max(max_s, dx * height[right])
                right -= 1
                
        return max_s
