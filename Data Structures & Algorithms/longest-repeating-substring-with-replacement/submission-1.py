class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        maxfreq = 0
        maxlen = 0
        start =0
        for end in range(len(s)):
            hashmap[s[end]]+=1
            maxfreq = max(maxfreq, hashmap[s[end]])

            while (end-start+1) -maxfreq >k:
                hashmap[s[start]]-=1
                start+=1
            maxlen = max(maxlen, end-start+1)
        return maxlen
            

            