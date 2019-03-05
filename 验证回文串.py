class Solution:
    # 需过滤非字母或数字
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = ''.join(filter(str.isalnum,s)).lower()
        return s==s[::-1]

    # def num_or_alpha(self, x):
    #     if ord('0') <= ord(x) <= ord('9') or \
    #         ord('a') <= ord(x) <= ord('z') or \
    #             ord('A') <= ord(x) <= ord('Z'):
    #         return True
    #     return False

    # def isPalindrome(self, s: str) -> bool:
    #     left = 0
    #     right = len(s) - 1
    #     s = s.lower()
    #     while left <= right:
    #         while left <= right and not self.num_or_alpha(s[left]):
    #             left += 1
    #         while left <= right and not self.num_or_alpha(s[right]):
    #             right -= 1
    #         if left <= right and s[left] == s[right]:
    #             left += 1
    #             right -= 1
    #         else:
    #             break
    #     if left < right:
    #         return False
    #     return True    
            
s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))