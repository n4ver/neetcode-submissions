class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        j = 0
        i = 0
        while i < n - j:
            if nums[i] == val:
                j += 1
                del nums[i]
            else:
                i += 1
        return i
