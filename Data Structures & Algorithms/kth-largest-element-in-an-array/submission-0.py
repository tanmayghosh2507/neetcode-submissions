import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Option 1: Using Heap
        heap = []
        for num in nums:
            if len(heap) >= k and heap[0] > num:
                continue
            
            heapq.heappush(heap, num)
            while len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]


        # Option 2: Using pivot index