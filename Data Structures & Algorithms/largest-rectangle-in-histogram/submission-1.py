class Solution:
    def largestRectangleArea(self, nums: List[int]) -> int:
        max_area = 0
        n = len(nums)
        left = [0]*n
        right = [0]*n
        stack = deque()

        # right smaller elements 
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop() 
            if stack:
                right[i] = stack[-1]
            else:
                right[i] = n
            stack.append(i)

        while stack:
            stack.pop()

        # left smaller elements 
        for i in range(n):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            else:
                left[i] = -1
            stack.append(i)
        
        #Calculate the Larget rectangle

        for i in range(n):
            width = right[i] - left[i] - 1
            curr_area = nums[i] * width
            max_area = max(max_area, curr_area)


        return max_area