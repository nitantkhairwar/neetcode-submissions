class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen1 = defaultdict(int)
        for num in s:
            seen1[num]+=1
        for num in t:
            if num in seen1 and seen1[num] > 0:
                seen1[num] -= 1
            else:
                return False
        return True
        