class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # (val, index)
        left_min_index = [i for i in range(n)]
        right_min_index = [i for i in range(n)]
        for index in range(n):
            i = index
            height = heights[i]
            while stack and stack[-1][0] >= height:
                _, i = stack.pop()
            stack.append((height, i))
            left_min_index[index] = i
        
        stack = []
        for index in range(n-1, -1, -1):
            i = index
            height = heights[i]
            while stack and stack[-1][0] >= height:
                _, i = stack.pop()
            stack.append((height, i))
            right_min_index[index] = i
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, (right_min_index[i] - left_min_index[i] + 1) * heights[i])
        
        return max_area