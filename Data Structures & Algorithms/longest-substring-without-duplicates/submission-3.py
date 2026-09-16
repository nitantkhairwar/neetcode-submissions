class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start =0
        d = set()
        maxlen = 0
        for end in range(len(s)):
            while s[end] in d:
                d.remove(s[start])
                start+=1
            d.add(s[end])
            maxlen = max(maxlen, end-start+1)
        return maxlen