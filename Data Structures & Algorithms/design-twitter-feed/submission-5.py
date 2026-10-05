class Twitter:

    def __init__(self):
        self.capacity = 10
        self.time = 0
        self.tweet_by_user = defaultdict(list) # user -> top 10 tweet []: heap
        self.followees = defaultdict(set) # user -> followee list []

    def postTweet(self, userId: int, tweetId: int) -> None:
        heap = self.tweet_by_user[userId]
        heap.append([self.time, tweetId])
        if len(heap) > self.capacity:
            heapq.heappop(heap)
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        for followee in self.followees[userId] | {userId}:
            for time, tweetId in self.tweet_by_user[followee]:
                heapq.heappush(heap, (time, tweetId))
        
        return [tid for _, tid in heapq.nlargest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followees[followerId].discard(followeeId)

        
