class MedianFinder:

    def __init__(self):
        self.left_heap = [] # max-heap
        self.right_heap = [] # min-heap

    def addNum(self, num: int) -> None:
        if len(self.left_heap) == 0 or num < (-1 * self.left_heap[0]):
            heapq.heappush(self.left_heap, -num)
        else:
            heapq.heappush(self.right_heap, num)
        
        if len(self.left_heap) - len(self.right_heap) >= 2:
            heapq.heappush(self.right_heap, -1 * self.left_heap[0])
            heapq.heappop(self.left_heap)
        elif len(self.right_heap) - len(self.left_heap) >= 2:
            heapq.heappush(self.left_heap, -1 * self.right_heap[0])
            heapq.heappop(self.right_heap)
        

    def findMedian(self) -> float:
        if len(self.left_heap) > len(self.right_heap):
            return -1 * self.left_heap[0]
        elif len(self.right_heap) > len(self.left_heap):
            return self.right_heap[0]
        else:
            return (-1 * self.left_heap[0] + self.right_heap[0])/2
        
        