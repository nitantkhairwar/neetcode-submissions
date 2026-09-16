class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        right = [0]*n
        left = [0]*n
        max_area = 0
        stack = []

        #right minimum
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n
            stack.append(i)

        # Reset stack
        stack.clear()

        #left minimum
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)

        for i in range(n):
            width = right[i] - left[i] -1
            curr_area = width*heights[i]
            max_area = max(curr_area, max_area)
        return max_area
        