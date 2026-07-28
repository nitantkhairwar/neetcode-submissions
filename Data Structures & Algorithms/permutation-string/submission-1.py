class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        counts_1 = [0]*26
        counts_2 = [0]*26

        if n1 > n2:
            return False

        for i in range(n1):
            counts_1[ord(s1[i]) - 97] += 1
            counts_2[ord(s2[i]) - 97] += 1
        
        if counts_1 == counts_2:
            return True
        
        for i in range(n1, n2):
            counts_2[ord(s2[i]) - 97] += 1
            counts_2[ord(s2[i - n1]) - 97] -= 1
            if counts_1 == counts_2:
                return True
        
        return False
        
            