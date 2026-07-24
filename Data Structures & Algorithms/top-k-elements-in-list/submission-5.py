class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i]+=1
        dic = dict(sorted(dic.items(), key = lambda x:x[1], reverse=True))
        
        return list(dic.keys())[:k]