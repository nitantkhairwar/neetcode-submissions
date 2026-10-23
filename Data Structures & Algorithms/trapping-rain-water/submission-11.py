class Solution:
    def trap(self, h: List[int]) -> int:
        n = len(h)
        left = [0]*n
        right = [0]*n
        max_water = 0

        left[0] = h[0]

        for i in range(1,n):
            left[i] = max(left[i-1], h[i])
            
        right[n-1] = h[n-1]

        for i in range(n-2, -1, -1):
            right[i] = max(right[i+1], h[i])
        
        for i in range(n):
            if h[i] <= min(right[i], left[i]):
                max_water+= min(right[i], left[i])- h[i]
        return max_water