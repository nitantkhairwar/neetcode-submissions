class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        maxlen = 0

        wordset = set(wordDict)

        for word in wordset:
            maxlen = max(maxlen, len(word))

        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1,n+1):
            for j in range(
                i-1,
                max(0, i-maxlen)-1,
                -1):
                if dp[j] and s[j:i] in wordset:
                    dp[i] = True
                    break

        return dp[n]
