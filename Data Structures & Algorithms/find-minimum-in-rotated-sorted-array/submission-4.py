class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        while l < r:
            midpoint = (r+l)//2
            if nums[midpoint] > nums[r]:
                l = midpoint + 1
            else:
                r = midpoint
        return nums[l]