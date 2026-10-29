class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        for num in nums:
            if count == 0: res = num
            if num == res: count += 1
            else: count -= 1
        return res

        '''
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        return max(seen, key=seen.get)
        '''