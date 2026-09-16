class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1>l2:
            return False
        
        c1 = Counter(s1)
        c2 = Counter(s2[:l1])
        if c1 == c2:
            return True
        start = 0
        end = l1
        for end in range(l1,l2): 
            c2[s2[end]]+=1
            # Remove element 
            c2[s2[start]]-=1
            if c2[s2[start]] == 0:
                del c2[s2[start]]
            if c1 == c2:
                return True
            start+=1
        return False
