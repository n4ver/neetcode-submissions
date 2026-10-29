class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        if len(nums) == 1: return True
        while r < len(nums):
            if (nums[l] + nums[r]) % 2 == 0: return False
            l += 1
            r += 1
        return True