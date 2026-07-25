class Solution:
    def trap(self, h: List[int]) -> int:
        max_water = 0
        for i in range(1,len(h)-1):
            lmax = max(h[:i])
            rmax = max(h[i:])
            if h[i] < min(lmax, rmax):
                max_water += min(lmax, rmax) - h[i]
        return max_water