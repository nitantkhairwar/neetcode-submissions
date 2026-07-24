class Solution:

    def encode(self, strs: List[str]) -> str:
        for i in range(len(strs)):
            strs[i] = str(len(strs[i]))+"#"+strs[i]
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j=j+1
            length = int(s[i:j])
            i = j+1
            res.append(s[i: i + length])
            i += length
        return res

