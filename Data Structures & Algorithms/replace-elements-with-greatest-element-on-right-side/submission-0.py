class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 1
        window = 0
        prev_max = 0
        res = [0] * n

        while i >= 0:
            if i == n-1:
                prev_max = arr[i]
                res[i] = -1
            else:
                res[i] = max(prev_max, arr[i+1])
                prev_max = res[i]
            i -= 1

        return res

