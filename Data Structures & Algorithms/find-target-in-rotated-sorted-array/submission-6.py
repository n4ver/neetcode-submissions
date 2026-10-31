class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l = 0
        r = n-1
        # Find the cut first
        while l < r:
            midpoint = (l+r)//2
            if nums[midpoint] > nums[r]: # The cut is somewhere on the right
                l = midpoint + 1
            else:
                r = midpoint
        pivot = l

            
        def binary_search(left, right):
            while left <= right:
                mid = (left+right)//2
                if nums[mid] == target:
                    return mid 
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        res = binary_search(0, pivot - 1)
        if res != -1: return res
        return binary_search(pivot, n-1)

