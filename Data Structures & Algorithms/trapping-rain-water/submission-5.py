class Solution:
    def trap(self, h: List[int]) -> int:
        n= len(h)
        l=0
        r = n-1
        lmax =0; rmax = 0

        ans = 0
        while(l<r):
            lmax = max(lmax, h[l])
            rmax = max(rmax, h[r])
            if lmax < rmax:
                ans += lmax - h[l]
                l+=1
            else:
                ans += rmax - h[r]
                r-=1
        return ans
