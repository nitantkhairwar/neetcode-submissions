class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        if l1>l2:
            return False
        
        c1 = Counter(s1)
        start = 0
        end = l1
        while end <= l2:
            if c1 == Counter(s2[start:end]):
                return True
            start+=1
            end+=1
        return False
