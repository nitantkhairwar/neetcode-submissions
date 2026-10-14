class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # A _ _ A _ _ A
        counts = Counter(tasks)

        maxfreq = max(counts.values())

        maxcount = 0

        for val in counts.values():
            if val == maxfreq:
                maxcount+=1
        
        intervals = (maxfreq-1)*(n+1)+ maxcount

        return max(len(tasks), intervals)
        