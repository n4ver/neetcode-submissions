class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        i = 0
        while i < len(nums):
            num = nums[i]
            if num not in seen:
                seen.add(num)
                i += 1
            else:
                nums.pop(i)

        return len(seen)

        