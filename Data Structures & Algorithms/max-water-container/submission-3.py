class Solution:
    def maxArea(self, h: List[int]) -> int:
        left = 0
        right = len(h)-1
        max_area = float("-inf")
        while left < right:
            n = right - left
            curr_area = min(h[left], h[right])*n
            if h[left]< h[right]:
                left +=1
            else:
                right -=1
            max_area = max(curr_area, max_area)
        return max_area