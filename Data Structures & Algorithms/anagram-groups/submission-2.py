class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for word in strs:
            lst = [0]*26
            for char in word:
                lst[ord(char)- ord('a')] += 1
            key = tuple(lst)    
            hashmap[key].append(word)
        return list(hashmap.values())