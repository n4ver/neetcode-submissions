class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        n = len(nums)
        seen = {}
        while i < n:
            if nums[i] not in seen:
                seen[nums[i]] = i
            else:
                if i - seen[nums[i]] <= k: return True
                else: seen[nums[i]] = i # Replace with latest value
            i += 1
        return False

                