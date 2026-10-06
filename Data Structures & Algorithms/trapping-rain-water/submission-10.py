class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0]*n
        right = [0]*n
        max_water = 0

        left[0] = height[0]
        for i in range(1,n-1):
            left[i] = max(left[i-1], height[i])
        
        right[n-1] = height[n-1]
        for i in range(n-2, 0, -1):
            right[i] = max(right[i+1], height[i])
        
        for i in range(1,n-1):
            if height[i] <= min(left[i], right[i]):
                max_water+= min(left[i], right[i])- height[i]
        return max_water