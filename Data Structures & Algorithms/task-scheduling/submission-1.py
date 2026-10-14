class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)

        maxfreq = max(counts.values())

        maxcount = 0

        for val in counts.values():
            if val == maxfreq:
                maxcount+=1
        
        result = (maxfreq-1)*(n+1)+ maxcount

        return max(len(tasks), result)
        