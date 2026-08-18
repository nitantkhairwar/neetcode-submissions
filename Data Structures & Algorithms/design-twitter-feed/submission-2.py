class Twitter:

    def __init__(self):
        self.feed = collections.defaultdict(list)
        self.fol = defaultdict(set)
        self.time =0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.feed[userId].append((tweetId, self.time))

    def getNewsFeed(self, userId: int) -> List[int]:
        users = self.fol[userId] | {userId}

        heap = []

        for uid in users:
            for tweetId, time in self.feed[uid][-10:]:
                heapq.heappush(heap, (-time, tweetId))
        res = []
        while heap and len(res) < 10:
            _, tweetId  = heapq.heappop(heap)
            res.append(tweetId)
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.fol[followerId].discard(followeeId)
