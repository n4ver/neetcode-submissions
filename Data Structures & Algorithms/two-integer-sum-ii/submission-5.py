class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1
        seen = set()
        while l < n:
            num1 = numbers[l]
            num2 = numbers[r]
            if num1 + num2 < target: # Since num2 is larger, we increment num1
                l += 1
            elif num1 + num2 > target:
                r -= 1
            else:
                return [l+1,r+1]
            


            
                