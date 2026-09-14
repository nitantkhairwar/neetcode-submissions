class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for char in strs:
            res += f"{len(char)}#{char}"
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i =0
        while i< len(s):
            j = i
            while s[j] != "#":
                j = j+1
            length = int(s[i:j])
            i = j+1
            res.append(s[i:i+length])
            i = i+length
        return res