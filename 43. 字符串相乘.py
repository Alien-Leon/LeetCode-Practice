class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        len1 = len(num1)
        len2 = len(num2)
        if len1 < len2:
            len1, len2, num1, num2 = len2, len1, num2, num1
        str1 = list(num1)
        str2 = list(num2)

        for i in range(len1):
            str1[i] = ord(str1[i]) - 48
        for i in range(len2):
            str2[i] = ord(str2[i]) - 48
        

        num = [0 for i in range(2*len(num1))]
        for j in range(len2-1, -1, -1):
            for i in range(len1-1, -1, -1):
                # print(str1[i] ,'*', str2[j])
                n = str1[i] * str2[j]
                up = int(n / 10)
                n %= 10
          
                # print(len2-1-j + len1-1-i)
                num[len2-1-j + len1-1-i] += n
                up += int(num[len2-1-j + len1-1-i] / 10)
                num[len2-1-j + len1-1-i] %= 10
                num[len2-1-j + len1-1-i + 1] += up
                # print(num[::-1])
        for i in range(len(num)):
            num[i] = chr(num[i]+48)
        num = num[::-1]
        # print(num)
        i = 0
        while i < len(num) and num[i] == '0':
            i += 1
        if i == len(num) and num[0] == '0':
            return '0'       
        return ''.join((num[i:]))
                 

s = Solution()

print(s.multiply('0', '0'))

