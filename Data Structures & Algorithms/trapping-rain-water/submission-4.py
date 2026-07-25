class Solution:
    def trap(self, h: List[int]) -> int:
        max_water = 0
        n = len(h)
        lmax = [0] * n
        rmax = [0] * n
        #leftmax array for array h 
        lmax[0] = h[0]
        for i in range(1,n-1):
            lmax[i] = max(h[i], lmax[i-1])

        #rightmax array for array h 
        rmax[n-1] = h[n-1]
        for i in range(n-2,0,-1):
            rmax[i] = max(h[i], rmax[i+1])

        for i in range(1,n-1):
            if h[i] <= min(lmax[i], rmax[i]):
                max_water += min(lmax[i], rmax[i]) - h[i]
        return max_water