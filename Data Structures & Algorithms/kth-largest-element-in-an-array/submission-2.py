import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Option 1: Using Heap
        # heap = []
        # for num in nums:
        #     if len(heap) >= k and heap[0] > num:
        #         continue
            
        #     heapq.heappush(heap, num)
        #     while len(heap) > k:
        #         heapq.heappop(heap)
        
        # return heap[0]

        # Option 2: Using pivot index
        # pivot = nums[0]
    
        # [2,3,1,5,4]
        # pivot = 2
        # [2,3,]
        # large_index = 1, curr_index = 2 -> 2 1 3 5 4, large_index = 2, curr_index = 2
        # swap(pivot_index, large_index - 1)

        target = len(nums) - k

        def quickSelect(l, r):
            pivot = nums[r]
            p = l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            
            nums[r], nums[p] = nums[p], nums[r]
            
            if p > target:
                return quickSelect(l, p - 1)
            elif p < target:
                return quickSelect(p + 1, r)
            else:
                return nums[p]
            
        
        return quickSelect(0, len(nums) - 1)