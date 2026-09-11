class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = defaultdict(int)
        for ch in s:
            dict1[ch]+=1
        
        dict2 = defaultdict(int)
        for ch in t:
            dict2[ch]+=1
        
        if len(dict1)!= len(dict2):
            return False
        
        for char in dict1:
            if dict1[char] != dict2[char]:
                return False
        return True