class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if n <= 1:
            return 0
        sorted_intervals = sorted(intervals, key=lambda interval: (interval[1], -interval[0]))

        # pick first interval
        picked = 1
        curr_end = sorted_intervals[0][1]
        for i in range(1, n):
            if sorted_intervals[i][0] >= curr_end:
                picked += 1
                curr_end = sorted_intervals[i][1]
        

        return n - picked