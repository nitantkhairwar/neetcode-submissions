class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        my_set = set(nums)
        max_length = 0
        for num in my_set:
            if num-1 not in my_set:
                curr_len = 1
                while num+1 in my_set:
                    curr_len += 1
                    num+=1
                max_length = max(max_length, curr_len)
        return max_length
