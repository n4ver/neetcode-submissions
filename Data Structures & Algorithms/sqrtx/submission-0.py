class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left+right)//2
            square = mid * mid
            if square > x: right = mid - 1
            elif square < x: left = mid + 1
            else: return mid

        return right