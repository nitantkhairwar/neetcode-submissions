class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = defaultdict(int)
        seen2 = defaultdict(int)
        for num in s:
            seen1[num]+=1
        for num in t:
            seen2[num]+=1
        return seen1 == seen2
        