class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}

        for i, char in enumerate(s):
            last[char] = i

        start = 0
        end = 0

        res = []

        for i, char in enumerate(s):
            end = max(end, last[char])
            if i == end:
                res.append(end- start+1)
                start= i+1
        return res
            