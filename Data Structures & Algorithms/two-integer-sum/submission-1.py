class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        i=0
        while True:
            diff = target - nums[i]
            if nums[i] in sum:
                    if diff in sum:
                        j = sum[diff]
                        if i != j:
                            if i > j:
                                return [j, i]
                            else:
                                return [i, j]
            else:
                sum[nums[i]] = i
            if i < len(nums) - 1:
                i += 1
            else:
                i = 0