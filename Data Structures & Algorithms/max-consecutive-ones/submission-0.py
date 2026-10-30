class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        res = 0
        while i < n:
            if nums[i] != 1:
                i += 1
                continue
            else:
                count = 0
                window = i
                while window < n and nums[window] == 1:
                    count += 1
                    window += 1
                res = max(count, res)
                i += 1
        return res

            