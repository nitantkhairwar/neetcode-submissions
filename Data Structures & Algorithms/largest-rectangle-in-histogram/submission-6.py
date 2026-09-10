class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        n = len(nums)
        stack = deque()
        left = [0]*n
        right = [0]*n
        max_area = 0

        #left minimum
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        
        # empty stack
        while stack:
            stack.pop()

        #right minimum

        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n
            stack.append(i)

        for i in range(n):
            width = right[i] - left[i] - 1
            curr_area = nums[i]*width
            max_area = max(max_area, curr_area)
        return max_area
            


        