class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        # Find the cut first
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: # Cut is on the right
                if target > nums[mid] or target < nums[l]: # If target is outside the left segment
                    l = mid + 1
                else: # if target is in the left segment
                    r = mid - 1
            else: # Cut is on the left
                if target < nums[mid] or target > nums[r]: # If target is outside the right segment
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
