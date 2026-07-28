class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1 = len(s)
        n2 = len(t)
        d = defaultdict(int)
        for char in t:
            d[char] += 1
        total = len(d); formed = 0
        l = r =0
        min_length = float("inf")

        while(r < len(s)):
            char = s[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    formed += 1

            while (l <= r ) and formed == total:
                curr_length = r - l + 1
                if curr_length < min_length :
                    min_length = curr_length
                    subl , subr = l , r+1
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1
                l += 1
            r += 1
        return "" if min_length == float("inf") else s[subl:subr]
