class Solution:
    def isPalindrome(self, x: int) -> bool:
        length = len(str(x))
        if x < 0: return False
        if length == 1: return True
        if x % 10 == 0: return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        
        if length % 2 == 0:
            return x == reversed_num
        else:
            return x == reversed_num // 10
        
        '''
        x_str = str(x)
        left = 0
        right = len(x_str) - 1
        while left <= right:
            if x_str[left] == x_str[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        '''