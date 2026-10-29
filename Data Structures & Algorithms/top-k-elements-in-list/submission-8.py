class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        res = []

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        heap = []
        for num in freq.keys():
            heapq.heappush(
                heap, 
                (freq[num], num)
            )
            if len(heap) > k: heapq.heappop(heap)

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res


        