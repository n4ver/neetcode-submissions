class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        sorted_nums = sorted(nums)
        res = []
        # [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]
        for k in range(n-2):
            # nums[k] + nums[i] + nums[j] = 0
            if k > 0 and sorted_nums[k] == sorted_nums[k-1]: continue
            i = k+1
            j = n - 1
            while i < j:
                total = sorted_nums[i] + sorted_nums[j] + sorted_nums[k]
                if total < 0: # potential numbers need to be GREATER
                    i += 1
                elif total > 0: # potential numbers need to be LOWER
                    j -= 1
                else:
                    res.append([sorted_nums[k],sorted_nums[i],sorted_nums[j]])
                    while i < j and sorted_nums[i] == sorted_nums[i+1]: i += 1
                    while i < j and sorted_nums[j] == sorted_nums[j-1]: j -= 1
                    i += 1
                    j -= 1
            
        return res
