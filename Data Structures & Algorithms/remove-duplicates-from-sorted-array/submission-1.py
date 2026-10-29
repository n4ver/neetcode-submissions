class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        k = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            if num not in seen:
                seen.add(num)
                k += 1
                i += 1
            else:
                nums.pop(i)

        return k

        