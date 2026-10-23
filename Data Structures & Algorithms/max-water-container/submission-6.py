class Solution:
    def maxArea(self, h: List[int]) -> int:
        max_area = float("-inf")
        left = 0
        right = len(h)-1
        n = len(h)-1
        while left < right:
            curr_area = min(h[left], h[right])*n

            if h[left] > h[right]:
                right-=1
            else:
                left+=1
            n-=1
            max_area = max(max_area, curr_area)

        return max_area
            